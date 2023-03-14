<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background: url(../asset/Type/3_1.jpg)">
        <div class="row">
          <div class="col-12">
            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">
                特警手语
              </h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Swat Sign Language</span>
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
              <h2 class="title">特警手语</h2>
              <span></span>
              <p>
                成人--------手臂向身旁伸出，手部抬起到胳膊高度，掌心向下。
                小孩--------手臂向身旁伸出，手肘弯曲，掌心向下固定放在腰间。
                女性嫌疑犯--掌心向着自己的胸膛，手指分开呈碗状，寓意是女性的胸部。
                人质--------用手卡住自己的脖子，寓意是被劫持的人质。
                指挥官------食指、中指、无名指并排伸直，横放在另一手臂上。
                手枪--------伸直大拇指及食指，互成90度，呈手枪姿势。
              </p>
              <p>
                自动武器------手指弯曲成抓状，在胸膛前上下扫动，像弹奏吉它一样。
                霰弹枪--------发信号的是手持霰弹枪的队员，只需用食指指指自己的武器便可。
                门口---------用食指由下方向上，向左再向下，作出开口矩形的手势，代表门口的形状。
                窗户--------用食指由下向上，向右，向下再向左作出一个闭合矩形的手势。
                听到--------举起手臂，手指间紧闭，拇指和食指触及耳朵。
              </p>
              <p>
                那里--------伸开手臂，用食指指向目标。
                掩护我------把手举到头上，弯曲手肘，掌心盖住天灵盖。
                放催泪弹----手指分开呈碗状，罩住面部的鼻子和嘴巴。
                集合--------手腕作握拳状，高举到头顶上，食指垂直向上竖起，缓慢地作圆圈运动。
                推进--------弯曲手肘部位，前臂指向地上，手指紧闭，从身后向前方摆动。
                明白--------手腕举到面额高度并作握拳状，掌心向着发指令者。
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
                src="../asset/Type/3_2.jpg"
                alt="About Image"
              />
              <img
                class="about-image-2 img-circle"
                src="../asset/Type/3_3.jpg"
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
  background: url(../asset/Type/3_1.jpg);
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
