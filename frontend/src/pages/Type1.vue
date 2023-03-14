<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background: url(../asset/Type/1_1.jpg)">
        <div class="row">
          <div class="col-12">
            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">
                中国手语
              </h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Chinese Sign Language</span>
                </li>
              </ul>
            </div>
            <!-- Breadcrumb wrapper End -->
          </div>
        </div>
      </div>
    </div>

    <!-- Breadcrumb Section End -->

    <!-- About Section Start -->
    <div class="section section-margin">
      <div class="container1">
        <div class="row m-b-n30 align-items-center">
          <div
            class="col-lg-6 m-b-30"
            data-aos="fade-up"
            data-aos-duration="1100"
          >
            <div class="about-content mw-100">
              <h2 class="title">中国手语</h2>
              <span></span>
              <p>
                古代就有手语的存在，并非专为聋人所有，古人靠手势来传达沟通意见，而后才慢慢产生语言。古人以打猎耕种为主，社会上需要遵循的规则也少，因此聋哑人较能适应生活，但文化发达后社会进步，抽象的符号也多，为了适应社会生活，只好藉手语来表达沟通情意了。
              </p>
              <p>
                手语历史悠久，但是正式的聋哑教育却是四百多年前才发展的，可考察到的是法国第一位伟大的聋教育家德雷佩神父，为了需要，自己创造发明手语以利管训工作。到了1760年他的收容所改为国立聋校，他被任命为第一任校长，他的助手认为应该编手语字典，也花很多时间致力于手语编辑工作，可惜手势太复杂，不能广泛被人使用，何况一个字有时往往需要用许多手势方能解释清楚，尤其抽象的表达更难，所以在1880年后只好改用口语法教学。
              </p>
              <p>
                1945年台湾光复，在台的日本老师被遣送回国，1949年大陆解放后，有些大陆聋校的老师栈台北启聪任教，于是台北混合了一些大陆语。左营启英聋校姜校长毕业于大陆启瘖学校，则采用大陆系手语。再加上聋胞散居各地，北、中、南三所聋校地区隔离，于是聋人所使用的手语逐渐现差异。2018年7月1日，中国实施《国家通用手语常用词表》和《国家通用盲文方案》作为语言文字规范发布。
              </p>
              <p>
                2021年3月1日，国家语委语言文字规范《〈中华人民共和国国歌〉国家通用手语方案》（GF0024-2020）正式实施。首次以听力残疾人手语使用者为主体，规范应用国家通用手语“唱”国歌，让听力残疾人切实体会国歌的真实内涵，从而和全国人民一同领略国歌激发民族爱国情感、催人奋进的巨大作用。该规范的实施切实解决了多年来听力残疾人手语使用者在奏唱国歌场合，规范、统一、严肃使用手语表达国歌的愿望，将使听力残疾人全面、准确感受国歌表现的民族精神，呼唤内心深处爱国主义情怀，促进我国残疾人文化、教育事业的繁荣发展。
              </p>
            </div>
          </div>
          <div
            class="col-lg-6 order-first order-lg-last m-b-30"
            data-aos="fade-up"
            data-aos-duration="1500"
          >
            <div class="about-image service-layer-image ms-auto">
              <img
                class="about-image-1"
                src="../asset/Type/1_3.jpg"
                alt="About Image"
              />
              <img
                class="about-image-2 img-circle"
                src="../asset/Type/1_2.jpg"
                alt="About Image"
              />
            </div>
          </div>
        </div>
      </div>
      <Footer class="foot"></Footer>
    </div>
    <!-- About Section End -->
  </div>
</template>

<script>
import Footer from "../components/Footer";

export default {
  name: "Type1",
  components: {
    Footer,
  },
};
</script>


<style scoped>
.foot {
  margin-top: 220px;
}

.head {
  z-index: 99;
}

.background_picture {
  height: 618px;
  background: url(../asset/Type/1_1.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  overflow: hidden;
  /*background-image: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);*/
}

.text-white {
  color: #fff !important;
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

.container {
  padding-right: 15px;
  padding-left: 15px;
  margin-left: 109px;
  margin-right: 109px;
  margin-top: 200px;
}

.container1 {
  padding-right: 15px;
  padding-left: 15px;
  margin-left: 109px;
  margin-right: 109px;
  margin-top: 100px;
}

.overlay::before {
  content: "";
  position: absolute;
  top: 60px;
  right: 0;
  bottom: 170px;
  left: 0;
  z-index: 1;
  background: -webkit-gradient(
    linear,
    left top,
    right top,
    from(rgba(20, 20, 20, 0.8)),
    color-stop(0%, rgba(20, 20, 20, 0.8))
  );
  background: -webkit-linear-gradient(
    left,
    rgba(20, 20, 20, 0.8) 0%,
    rgba(20, 20, 20, 0.8) 0%
  );
  background: -o-linear-gradient(
    left,
    rgba(20, 20, 20, 0.8) 0%,
    rgba(20, 20, 20, 0.8) 0%
  );
  background: linear-gradient(
    to right,
    rgba(20, 20, 20, 0.8) 0%,
    rgba(20, 20, 20, 0.8) 0%
  );
}

.container {
  max-width: 1200px;
}

.row {
  --bs-gutter-x: 30px;
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

.col-12 {
  flex: 0 0 auto;
  width: 100%;
}

.breadcrumb-wrapper {
  text-align: center;
  position: relative;
  z-index: 99;
  padding-top: 40px;
}

.about-content {
  text-align: left;
}

.about-content span {
  position: relative;
  margin-top: 20px;
  padding-bottom: 30px;
  display: block;
  text-align: left;
}

.about-content span:after {
  position: absolute;
  content: "";
  width: 60px;
  height: 1px;
  background: #a295df;
}

.breadcrumb-wrapper .title {
  font-weight: 400;
  font-size: 56px;
  margin-bottom: 0;
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
  list-style-type: disc;
}

ul li {
  list-style: none;
}

.breadcrumb-wrapper .breadcrumb-menu li span {
  color: #ffffff;
  font-size: 16px;
}

.section-margin {
  margin-top: 0px;
  margin-bottom: 0px;
}

.section,
.section-fluid {
  float: left;
  width: 100%;
}

.m-b-n30 {
  margin-bottom: -30px;
}

.row {
  --bs-gutter-x: 30px;
}

.align-items-center {
  align-items: center !important;
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

.aos-animate {
  opacity: 1;
  transform: translateZ(0);
}

.col-lg-6 {
  flex: 0 0 auto;
  width: 50%;
}

.mw-100 {
  max-width: 100% !important;
}

h2 {
  font-size: 36px;
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

p {
  margin-top: 0;
  margin-bottom: 1rem;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  color: #8a8a8a;
  line-height: 2;
  visibility: visible;
}

.service-layer-image {
  position: relative;
  height: 577px;
}

.about-image {
  max-width: 530px;
  margin-left: -100px;
}

.ms-auto {
  margin-left: 0px;
}

.service-layer-image .about-image-1 {
  -webkit-box-shadow: #959ea5 0px 0px 41px;
  box-shadow: #959ea5 0px 0px 41px;
  border-radius: 50px;
}

.service-layer-image .about-image-2 {
  position: absolute;
  right: 0px;
  top: 255px;
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
</style>
