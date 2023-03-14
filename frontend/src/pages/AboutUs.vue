<template>
  <div>
    <div>
      <Main></Main>
    </div>
    <div>
      <About></About>
    </div>
    <div>
      <About2></About2>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import Carousel from "../components/Carousel";
import Footer from "../components/Footer";
import Main from "../components/Main";
import About from "../components/About";
import About2 from "../components/About2";
export default {
  name: "AboutUs",
  components: { About2, About, Main, Footer, Carousel, Navbar },
};
</script>

<style scoped>
</style>
