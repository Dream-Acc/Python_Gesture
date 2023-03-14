<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background: url(../asset/Type/2_1.jpg)">
        <div class="row">
          <div class="col-12">
            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">指唇语</h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Finger Lip Language</span>
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
              <h2 class="title">指唇语</h2>
              <span></span>
              <p>
                《指唇语》，它是用右手声母和唇型韵母(或附加左手韵母)来辅助汉语口语教学的一种手语方案。特点是:手口并用，侧重"声(介)母+唇型"手语模式，兼顾单、双手使用，适用于聋人家庭和学校口语教学。指型文，作为记录双手指语的书面符号，可应用于各种场所的聋人无障碍标识。
              </p>
              <p>
                我国民间有传统数字手语，即一指一、二指二、三指三、四指四、五指五、挠六、捏七、杈八、钩九、握拳零，数字手语的指式是:食指一指伸开表示数码1;中指和食指二指伸开表示数码2;中指、食指和拇指三指伸开表示数码3;食指、中指、无名指和小指四指伸开表示数码4;五指全部伸开表示数码5;五指半弯、呈"挠"指状表示数码6;中食拇三指半弯、对齐呈"捏"指状表示数码7;拇指和食指二指伸开呈"杈"状表示数码8;食指一指半弯、呈"钩"状表示数码9;五指收拢、呈"拳"状表示数码0。《指唇语》方案里的声、韵母指式来源于上述指法规范。
              </p>
              <p>
                《指唇语》方案如下:
                指式和手位起始:五指并拢半弯、中食拇指尖对齐，放在脸前5cm位置。
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
                src="../asset/Type/2_2.jpg"
                alt="About Image"
              />
              <img
                class="about-image-2 img-circle"
                src="../asset/Type/2_3.jpg"
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
  background: url(../asset/Type/2_1.jpg);
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
