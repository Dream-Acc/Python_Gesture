<template>
  <div>
    <Header></Header>
    <div
      class="background_picture section breadcrumb-section overlay"
      data-bg-image="../asset/Character/2_1.jpg"
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
                社会性
              </h1>

              <ul
                class="breadcrumb-menu"
                data-aos="fade-up"
                data-aos-duration="1500"
              >
                <li>
                  <span>Sociality</span>
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
                  src="../asset/Character/2_2.jpg"
                  alt="Blog Details"
                />
              </div>

              <h2
                class="blog-details-title m-b-20"
                data-aos="fade-up"
                data-aos-duration="1300"
              >
                社会性
              </h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                苏联的语言学家马尔(Mapp)也认为人类开始时只有"手的语言"，(《语言学系列教材
                应用语言学》桂诗春 (湖南教育出版社
                1988年5月第1版))后来才被有声语言代替。正是古代猿人的直立行走、前肢变为手，使得猿人用身势语进行交流成为可能，由于生理上的进化和交流的需要，逐渐产生了有声语言，而作为没有声音的听障人和语言障碍者来说，随着社会的进化和语言的发展，手势语越来越丰富、规范，而成为现代独立的一种语言。
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
                    src="../asset/Character/2_3.jpg"
                    alt=""
                  />
                </div>
                <div
                  class="blog-content m-b-50"
                  data-aos="fade-up"
                  data-aos-duration="1600"
                >
                  <p>
                    自60年代以来，由于欧美两地对听障人手语的重视并且正式把它作为语言研究的一个对象，使得手语在欧美国家已经作为语言的一个种类而进行研究。在欧美，不光是听障人和语言障碍者要学习手语，对于接触听障人和语言障碍者比较多的人来说，他们同样也在学习手语，以便与听障人和语言障碍者更好地交流，更好地为听障人服务，促进了手语的进一步发展。
                    手语是约定俗成的产物。"约定"的意思品"共同议定"，"俗成"的意思是"大众中形成的风俗习惯"。当然，这里的"共同"最初是由听障人和语言障碍者自己在生活和交流中双方都能理解的手势，当形成大家都能理解时，则形成了一种默契，在听障人和语言障碍者中形成了一定的习惯。随着社会和语言的发展，由于教育者和研究者的加入，对听障人和语言障碍者手语进行归纳、研究和创造，使得手语的词汇量不断丰富，手语不断的规范化，形成了现在的这种手势语言。
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
  background: url(../asset/Character/2_1.jpg);
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
