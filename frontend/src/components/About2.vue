<template>
  <div
    class="responsibility-wrapper slide-out slide-out--active"
    id="responsibility"
  >
    <div class="responsibility">
      <h2 class="responsibility__title">项目介绍</h2>
      <p class="responsibility__title-en">PROJECT INTRODUCTION</p>
    </div>

    <div class="about">
      <img
        class="about__img"
        src="https://media-image1.baydn.com/storage_media_image/kzlbpl/b2b1c0845c63b012547d5be15c7e5b07.7ce09bfd8b123cb7c22dbf854e7fe953.png?x-oss-process=image/format,jpg/quality,q_80"
        alt="about"
      />

      <div class="about__info">
        <p class="about__title-en"></p>
        <h2 class="about__title"></h2>
        <p class="about__content">
          项目旨在为更多有需要的人群免费普及手语，将手语进行推广。手语课堂模块为用户普及手语的发展历程、种类以及手语的特点；单词模块为用户提供各种词语的动作要领、手语视频以及开启摄像头检测用户手语动作是否标准；测试模块在每个词语都为用户提供熟识、忘记两个选项，点击熟识进入下一个词语的检测，点击一次忘记出现动作要领的文字提示，点击第二次出现手语视频；生词模块可查看用户熟悉度不高的词语。
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About2",
};
</script>

<style scoped>
.slide-out {
  will-change: transform, opacity;
}
.responsibility-wrapper {
  margin-top: 32px;
  padding: 45px 0 73px;
  background-color: #fff;
}
.responsibility {
  width: 944px;
  margin: 0 auto;
  text-align: center;
}
* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
.slide-out--active .responsibility__title,
.slide-out--active .responsibility__title-en {
  -webkit-transform: translateY(0);
  -ms-transform: translateY(0);
  transform: translateY(0);
  opacity: 1;
}
.slide-out .responsibility__title {
  -webkit-transition: opacity 1s ease-in-out 0.1s,
    -webkit-transform 1s ease-in-out 0.1s;
  transition: opacity 1s ease-in-out 0.1s, -webkit-transform 1s ease-in-out 0.1s;
  -o-transition: transform 1s ease-in-out 0.1s, opacity 1s ease-in-out 0.1s;
  transition: transform 1s ease-in-out 0.1s, opacity 1s ease-in-out 0.1s;
  transition: transform 1s ease-in-out 0.1s, opacity 1s ease-in-out 0.1s,
    -webkit-transform 1s ease-in-out 0.1s;
}
.responsibility__title {
  position: relative;
  z-index: 1;
  display: inline-block;
  color: #333;
  font-weight: 500;
  font-size: 32px;
  line-height: 45px;
  -webkit-transform: translateY(40px);
  -ms-transform: translateY(40px);
  transform: translateY(40px);
  opacity: 0;
}
h1,
h2,
h3,
h4,
p {
  margin: 0;
}
.responsibility__title:after {
  position: absolute;
  top: -4px;
  left: -13px;
  z-index: -1;
  width: 33px;
  height: 33px;
  background-image: -webkit-linear-gradient(
    322deg,
    #d6efe7 14%,
    rgba(214, 239, 231, 0) 112%
  );
  background-image: -o-linear-gradient(
    322deg,
    #d6efe7 14%,
    rgba(214, 239, 231, 0) 112%
  );
  background-image: linear-gradient(
    128deg,
    #d6efe7 14%,
    rgba(214, 239, 231, 0) 112%
  );
  border-radius: 50%;
  content: "";
}
.responsibility__title-en {
  margin-top: 4px;
  color: #ccc;
  font-size: 20px;
  line-height: 28px;
  text-align: center;
  -webkit-transform: translateY(40px);
  -ms-transform: translateY(40px);
  transform: translateY(40px);
  opacity: 0;
}
.slide-out {
  will-change: transform, opacity;
}

.responsibility__tab li {
  cursor: pointer;
}

.slide-out {
  will-change: transform, opacity;
}

a {
  color: #28bea0;
  text-decoration: none;
}
a {
  background-color: transparent;
}
img {
  max-width: 100%;
}
img {
  border-style: none;
}

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
  margin-left: 40px;
  position: relative;
  margin-top: 30px;
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
  margin-left: 40px;
  margin-right: 40px;
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
  paddding-left: 40px;
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
</style>
