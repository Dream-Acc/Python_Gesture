<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background: url(../asset/Type/4_1.jpg)">
        <div class="row">
          <div class="col-12">
            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">
                双拼掌语
              </h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Double Spell Palm Language</span>
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
              <h2 class="title">双拼掌语</h2>
              <span></span>
              <p>
                双拼掌语，以掌语人假定的四个屋角为参照系，也称屋角掌语;在双拼掌语过程中，如果手臂动作幅度达到直伸程度，即可转化为双拼臂语。相比指语拼音，双拼掌语两次手语动作表达一个字音，字母动作清楚，有效交流距离更远，可供听障人，语言障碍者，手语教师等人群使用。
              </p>
              <p>
                2018年5月21日，《国家通用手语常用词表》和《国家通用盲文方案》由国家语言文字工作委员会规范标准审定委员会审定，经中国残疾人联合会、教育部、国家语言文字工作委员会同意，作为语言文字规范发布，自2018年7月1日起实施。
              </p>
              <p>
                相较于原《中国手语》，《国家通用手语常用词表》明显地收录了广大听力残疾人现实生活中广泛使用的手语，替换了过去许多和汉字一一对应的手语，大量减少了手指字母的使用，注意描述手语表达时体态动作和面部表情的变化，重在体现手语表形表意的语言特点。
              </p>
              <p>
                《国家通用盲文方案》沿用了现行盲文的声母、韵母、声调和标点符号，没有改变、删减或增加任何一个符号，只是完善了现行盲文标调规则，规范了声调符号的用法。国家通用盲文能够与现行盲文平稳、顺利地实现新旧过渡。学习了国家通用盲文的人，如果要阅读以前旧版现行盲文书籍，无需准备性学习。
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
                src="../asset/Type/4_2.jpg"
                alt="About Image"
              />
              <img
                class="about-image-2 img-circle"
                src="../asset/Type/4_3.jpg"
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
  background: url(../asset/Type/4_1.jpg);
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
