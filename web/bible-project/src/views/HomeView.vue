<script default lang="ts">
    import axios from "axios";

    export default {
       data() {
        return {
           teste: {} 
        }
       },
       created() {
          axios.get(`http://localhost:8000/versicle`)
               .then((response) => {
                    console.log(response);
                    this.teste = response.data;
                    console.log(this.teste);
               })
               .catch((e) => {
                   console.log(e);
               });
       }
    }
</script>

<template>
  <main>
      {{teste.versicle}}
  </main>
</template>
