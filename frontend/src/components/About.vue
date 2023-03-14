<template>
  <div class="about-wrapper slide-out slide-out--active" id="about">
    <div class="about">
      <img
        class="about__img"
        src="https://media-image1.baydn.com/storage_media_image/cassho/dc39b28d95576d5c8fd0c26b54bfc1ae.4a92a2b171562d0272b837c1ea2a1990.png?x-oss-process=image/format,jpg/quality,q_80"
        alt="about"
      />
      <div class="about__info">
        <p class="about__title-en">ABOUT SHOUZHISHENG</p>
        <h2 class="about__title">关于手之声</h2>
        <p class="about__content">
          手之声是专门帮助聋哑人士学习手语的平台，通过该平台的学习可以让聋哑人士掌握较为基础的手语手势，并通过开启摄像头的方式将手势同手势库进行相似度匹配，获得更为精准的学习体验。
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
};
</script>

<style scoped>
.slide-out {
  will-change: transform, opacity;
}

.about-wrapper {
  padding: 72px 0;
  background: #f7f7f7;
}

.about {
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 944px;
  margin: 0 auto;
  padding: 24px 30px 24px 24px;
  background-color: #fff;
}

.about__img {
  width: 480px;
  height: 348px;
}

img {
  max-width: 100%;
  border-style: none;
}

.about__title-en {
  color: #ccc;
  font-size: 18px;
  line-height: 25px;
}

h1,
h2,
h3,
h4,
p {
  margin: 0;
}

.about__title {
  position: relative;
  margin-top: 4px;
  color: #333;
  font-weight: 500;
  font-size: 32px;
}

.about__title:after {
  position: absolute;
  bottom: -12px;
  left: 0;
  width: 32px;
  height: 4px;
  background-color: #209e85;
  content: "";
}

.about__content {
  margin-top: 52px;
  color: rgba(51, 51, 51, 0.65);
  line-height: 30px;
  letter-spacing: 0.5px;
  text-align: justify;
  text-indent: 2em;
}

.about:after {
  -webkit-transform: translateY(0);
  -ms-transform: translateY(0);
  transform: translateY(0);
  opacity: 1;
}

.about:after,
body.pixel .slide-out .about__info {
  -webkit-transition: opacity 1s ease-in-out 0.4s,
    -webkit-transform 1s ease-in-out 0.4s;
  transition: opacity 1s ease-in-out 0.4s, -webkit-transform 1s ease-in-out 0.4s;
  -o-transition: transform 1s ease-in-out 0.4s, opacity 1s ease-in-out 0.4s;
  transition: transform 1s ease-in-out 0.4s, opacity 1s ease-in-out 0.4s;
  transition: transform 1s ease-in-out 0.4s, opacity 1s ease-in-out 0.4s,
    -webkit-transform 1s ease-in-out 0.4s;
}

.about:after {
  position: absolute;
  right: 30px;
  bottom: 24px;
  width: 15px;
  height: 15px;
  border-right: 2px solid #209e85;
  border-bottom: 2px solid #209e85;
  content: "";
}
.about__info {
  margin-left: 40px;
}

.about {
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 944px;
  margin: 0 auto;
  padding: 24px 30px 24px 24px;
  background-color: #fff;
}
</style>
