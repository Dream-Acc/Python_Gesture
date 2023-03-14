<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<script>
import Navbar from "./components/Navbar"
export default {
  name: 'App',
  components: {Navbar},
  created() {
  if (sessionStorage.getItem('store')) {
    this.$store.replaceState(Object.assign({}, this.$store.state, JSON.parse(sessionStorage.getItem('store'))));
  }
  window.addEventListener('beforeunload', () => {
    sessionStorage.setItem('store', JSON.stringify(this.$store.state));
  });
}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
