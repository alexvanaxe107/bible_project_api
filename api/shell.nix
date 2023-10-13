{ pkgs ? import <nixpkgs> {} }:
  # ENV Variables

  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ python3 sqlite postgresql ];


    # LD_LIBRARY_PATH = "${geos}/lib:${gdal}/lib";

    shellHook = ''
    source .venv/bin/activate
    export PGDATA="$PWD/.pg"

    _start_pg(){
        pg_ctl -w -l $PGDATA/log -o "--unix_socket_directories=$PWD" start &> /dev/null
    }
    _stop_pg(){
        pg_ctl stop &> /dev/null
    }


    if [ ! -d $PGDATA ]; then
        initdb &> /dev/null
        CREATE=true
    fi

    _start_pg
    # register_cleanup _stop_pg # ~ trapping HUP/EXIT

    if [[ $CREATE ]]; then
        createuser -s postgres &> /dev/null
        # set a stable crappy password for local/dev
        # create db
    fi
    '';
}
