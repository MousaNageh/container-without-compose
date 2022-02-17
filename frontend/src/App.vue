<template>
  <div id="app">
    <pre v-if="data">
      {{JSON.stringify(data,null)}}
    </pre>
    <button @click="getData">hello from </button>
    
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return{
      data:null
    }
  },

  methods:{
    getData(){
      fetch("http://localhost:8000/test")
      .then(res=>res.json())
      .then(data=>{
        this.data = data
      })
    }
  }
  


}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
