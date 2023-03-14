<template>
  <div class="banner">
    <img
      class="banner__img"
      src="https://media-image1.baydn.com/storage_media_image/cassho/c84cb410e2c66a7f8bb4356a8c909647.1204db12e0f405fc93de2f4529187442.png?x-oss-process=image/format,jpg/quality,q_80"
      alt="让每个人都能通过学习变得更好"
    />
    <h1 class="banner__slogan">让每个人都能通过学习变得更好</h1>
  </div>
</template>

<script>
export default {
  name: "Main",
};
</script>

<style scoped>
body.pixel .banner {
  position: relative;
  height: 0;
  padding-bottom: 46.67%;
  text-align: center;
}
* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
body.pixel .banner__img {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  -o-object-fit: cover;
  object-fit: cover;
}
img {
  max-width: 100%;
  border-style: none;
}

body.pixel .banner__logo {
  position: absolute;
  bottom: 40px;
  width: 100px;
  margin: 0 auto;
}
.banner__slogan {
  position: absolute;
  top: 40%;
  left: 50%;
  width: 100%;
  color: rgba(255, 255, 255, 0.85);
  font-weight: 300;
  font-size: 56px;
  letter-spacing: 3.5px;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>
