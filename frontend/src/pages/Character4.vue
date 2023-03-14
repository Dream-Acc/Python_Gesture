<template>
  <div>
    <Header></Header>
    <div
      class="background_picture section breadcrumb-section overlay"
      data-bg-image="../asset/Character/4_1.jpg"
    >
      <div class="container">
        <div class="row">
          <div class="col-12">
            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1
                class="title text-white"
                data-aos="fade-up"
                data-aos-duration="1100"
              >
                规律性
              </h1>

              <ul
                class="breadcrumb-menu"
                data-aos="fade-up"
                data-aos-duration="1500"
              >
                <li>
                  <span>Regularity</span>
                </li>
              </ul>
            </div>
            <!-- Breadcrumb wrapper End -->
          </div>
        </div>
      </div>
    </div>
    <!-- Breadcrumb Section End -->

    <!-- Blog Grid Section Start -->
    <div class="section section-margin">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 m-auto p-lg-0">
            <div class="blog-details-wrapper">
              <div
                class="blog-details-image m-b-40"
                data-aos="fade-up"
                data-aos-duration="1100"
              >
                <img
                  class="img-circle img-shadow"
                  src="../asset/Character/4_2.jpg"
                  alt="Blog Details"
                />
              </div>

              <h2
                class="blog-details-title m-b-20"
                data-aos="fade-up"
                data-aos-duration="1300"
              >
                规律性
              </h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                手势的起源是和人类社会一起产生的，而把手势作为一种语言，它的产生和发展是则和聋人教育同步的。在没有聋人学校之前，社会的个体的简单的形象根本不称为手势语。聋教育的发展，教学上的需要和听障人和语言障碍者彼此的需要，使手势语的词汇逐渐增加并形成它的言语规律，进而形成了一种语言。
              </p>
              <p class="text" data-aos="fade-up" data-aos-duration="1100"></p>

              <div class="blog-content-image m-t-40 m-b-n50">
                <div
                  class="blog-content-thumb m-b-50"
                  data-aos="fade-up"
                  data-aos-duration="1400"
                >
                  <img
                    class="img-circle img-shadow"
                    src="../asset/Character/4_3.jpg"
                    alt=""
                  />
                </div>
                <div
                  class="blog-content m-b-50"
                  data-aos="fade-up"
                  data-aos-duration="1600"
                >
                  <p>
                    长期以来，国内外一些聋教育工作者一直关注手语，开展了理论性和应用性的研究，发表了论文、专著。从手语的形式和内容等方面证明手语的语言价值和地位，从手语构成的表意法(摩状、会意、指示、借代、综合等)、构词法(词根、词缀)、造句法(所谓"倒装句"、"省略句")三方面作了初步分类、归纳、整理，认识了手语的结构体系。
                    上海教育学院蔡浩中在《简论聋人手势语的构成要素》(《现代特殊教育》1994.1第11页)中认为手语词类有名词、代词、动词、形容词、数词、副词、连词、介词、助词等，但不用量词，没有叹词，而且词的兼类现象较多，手语句子有主、谓、宾、定、状、补等句子成分，有主谓、主动宾、主动补等句子的结构，有宾语前置、定语倒置、状语倒置、省略介词等常见特点。
                    手语的词根和词缀是不同于汉语的，词根和词缀是根据手的形状来产生的。
                  </p>
                  <p></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer class="foot"></Footer>
    </div>
    <!-- Blog Grid Section End -->
  </div>
</template>

<script>
import Footer from "../components/Footer";

export default {
  name: "Character1",
  components: {
    Footer,
  },
};
</script>


<style scoped>
.foot {
  margin-top: 220px;
}

.background_picture {
  height: 618px;
  background: url(../asset/Character/4_1.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  overflow: hidden;
  /*background-image: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);*/
}

.breadcrumb-section {
  height: 650px;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
}

.section,
.section-fluid {
  float: left;
  width: 100%;
}

.overlay {
  position: relative;
}

.overlay::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  background: linear-gradient(
    to right,
    rgba(20, 20, 20, 0.8) 0%,
    rgba(20, 20, 20, 0.8) 0%
  );
}

.container {
  max-width: 1200px;
  padding-right: var(--bs-gutter-x, 15px);
  padding-left: var(--bs-gutter-x, 15px);
  width: 100%;
  margin-right: auto;
  margin-left: auto;
}

.row {
  --bs-gutter-x: 30px;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

.col-12 {
  flex: 0 0 auto;
  width: 100%;
}

.row > * {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) / 2);
  padding-left: calc(var(--bs-gutter-x) / 2);
  margin-top: var(--bs-gutter-y);
}

.breadcrumb-wrapper {
  text-align: center;
  position: relative;
  z-index: 99;
  padding-top: 40px;
}

.breadcrumb-wrapper .title {
  font-weight: 400;
  font-size: 56px;
  margin-bottom: 0;
}

.text-white {
  color: #fff !important;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Vidaloka", serif;
  font-weight: 600;
  line-height: 1.2;
  color: #232324;
}

.breadcrumb-wrapper .breadcrumb-menu {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  margin-top: 30px;
}

ul {
  margin: 0;
  padding: 0;
}

ul li {
  list-style: none;
}

.breadcrumb-wrapper .breadcrumb-menu li span {
  color: #ffffff;
  font-size: 16px;
}

.section-margin {
  margin-top: 120px;
  margin-bottom: 0px;
}

.section,
.section-fluid {
  float: left;
  width: 100%;
}

.container {
  padding-right: var(--bs-gutter-x, 15px);
  padding-left: var(--bs-gutter-x, 15px);
}

.row {
  --bs-gutter-x: 1.5rem;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

h2 {
  font-family: "Vidaloka", serif;
  font-weight: 600;
  line-height: 1.2;
  color: #232324;
  font-size: 36px;
}

.p-lg-0 {
  padding: 0 !important;
}

.m-auto {
  margin: auto !important;
}

.col-lg-8 {
  flex: 0 0 auto;
  width: 66.6666666667%;
}

.m-b-40 {
  margin-bottom: 40px;
}

.img-shadow {
  box-shadow: #959ea5 0px 0px 41px;
}

.img-circle {
  border-radius: 50px;
}

img {
  max-width: 100%;
}

img,
svg {
  vertical-align: middle;
}

p {
  margin-top: 0;
  margin-bottom: 1rem;
  text-align: left;
}

.blog-details-wrapper .blog-content-image {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
}

.m-b-n50 {
  margin-bottom: -50px;
}

.m-t-40 {
  margin-top: 40px;
}

.blog-details-wrapper .blog-content-image .blog-content-thumb {
  margin-right: 40px;
  width: 360px;
}

.blog-details-wrapper .blog-content-image .blog-content-thumb img {
  max-width: 100%;
  width: 100%;
  display: block;
}

.blog-details-wrapper .blog-content-image .blog-content {
  width: calc(100% - 360px);
}

.blog-details-wrapper p {
  color: #4f4f4f;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  line-height: 2;
  visibility: visible;
}
</style>
