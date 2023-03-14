<template>
  <div>
    <Header></Header>
    <div
      class="background_picture section breadcrumb-section overlay"
      data-bg-image="../asset/Character/3_1.jpg"
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
                实用性
              </h1>

              <ul
                class="breadcrumb-menu"
                data-aos="fade-up"
                data-aos-duration="1500"
              >
                <li>
                  <span>Practicability</span>
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
                  src="../asset/Character/3_2.jpg"
                  alt="Blog Details"
                />
              </div>

              <h2
                class="blog-details-title m-b-20"
                data-aos="fade-up"
                data-aos-duration="1300"
              >
                实用性
              </h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                手语是听障人和语言障碍者之间的交际工具，这是任何人都知道的。这种手语和摩尔所说的"姿势语言"是不同的。"姿势语言"使人们之间用来暂时的表达情感、态度等动作，而作为现代意义的手语则是经过了约定俗成的听障人和语言障碍者之间能够共同使用、相互理解的交际工具，经过了研究者和教育者的研究和规定，用一定的规律，构词法则，手势的命名规范。
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
                    src="../asset/Character/3_3.jpg"
                    alt=""
                  />
                </div>
                <div
                  class="blog-content m-b-50"
                  data-aos="fade-up"
                  data-aos-duration="1600"
                >
                  <p>
                    听障人和语言障碍者也是能够思维的。听障人语言障碍者和常人一样，生活在人类社会中，有健全的大脑和发育器官，人们的大脑分左右两半球，各有专门的分工。他们主要是因为耳聋听不见别人说话，才学不会语言。一旦恢复或获得了听觉，听障人和语言障碍者也就可以逐渐学会说话。其次，大脑是人的一切活动的司令部，人的各种感觉器官由它统一组成一个完整的体系。
                    交际工具分语言的交际工具和身势等非活言的交际工具，听障人和语言障碍者既然得不到语言的交际工具就发展非语言的交际工具，从视觉、感觉等去接收常人用听觉得到的信息。听障人和语言障碍者视觉很灵，通常用手势来表达意思。第三，
                    "眼观六面耳听八方"，听觉获得信息的可能性比视觉大得多，通过视觉的交际，效果究竟不如有声语言，这不能不给听障人和语言障碍者思维能力的发展带来影响。
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
  background: url(../asset/Character/3_1.jpg);
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
