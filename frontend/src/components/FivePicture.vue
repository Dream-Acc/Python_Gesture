<template>
  <!-- 5张图 -->
  <div class="picture6">
    <div class="row picture6-main" style="padding-top: 10vh">
      <div class="col-12 col-sm-12 overflow-hidden">
        <div class="carousel slide" id="carousel-demo" data-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div class="row row-cols-1 row-cols-md-5">
                <div class="col">
                  <img
                    src="../asset/FivePicture/11.jpg"
                    class="d-block w-100 img-thumbnail img-ex"
                  />
                </div>
                <div class="col">
                  <img
                    src="../asset/FivePicture/12.webp.jpg"
                    class="d-block w-100 img-thumbnail img-ex"
                  />
                </div>
                <div class="col">
                  <img
                    src="../asset/FivePicture/13.webp.jpg"
                    class="d-block w-100 img-thumbnail img-ex"
                  />
                </div>
                <div class="col">
                  <img
                    src="../asset/FivePicture/14.webp.jpg"
                    class="d-block w-100 img-thumbnail img-ex"
                  />
                </div>
                <div class="col">
                  <img
                    src="../asset/FivePicture/15.webp.jpg"
                    class="d-block w-100 img-thumbnail img-ex"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FivePicture",
};
</script>

<style scoped>
.picture6 {
  width: 1233px;
  margin: 0 auto;
  padding-bottom: 39px;
}

.picture6-main {
  margin: 0 auto;
}

.img-ex {
  height: 160px;
}

.row {
  padding-top: 5px !important;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}

.col-sm-12 {
  -ms-flex: 0 0 100%;
  flex: 0 0 100%;
  max-width: 100%;
}
.col-12 {
  -ms-flex: 0 0 100%;
  flex: 0 0 100%;
  max-width: 100%;
}

.carousel {
  position: relative;
}

.carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.carousel-indicators li {
  box-sizing: content-box;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  width: 30px;
  height: 3px;
  margin-right: 3px;
  margin-left: 3px;
  text-indent: -999px;
  cursor: pointer;
  background-color: #fff;
  background-clip: padding-box;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  opacity: 0.5;
  transition: opacity 0.6s ease;
}
.carousel-item-next,
.carousel-item-prev,
.carousel-item.active {
  display: block;
}
.carousel-item {
  position: relative;
  display: none;
  float: left;
  width: 100%;
  margin-right: -100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  transition: -webkit-transform 0.6s ease-in-out;
  transition: transform 0.6s ease-in-out;
  transition: transform 0.6s ease-in-out, -webkit-transform 0.6s ease-in-out;
}

.row-cols-md-5 > * {
  -ms-flex: 0 0 20%;
  flex: 0 0 20%;
  max-width: 20%;
}
.row-cols-1 > * {
  -ms-flex: 0 0 100%;
  flex: 0 0 100%;
  max-width: 100%;
}
.col {
  -ms-flex-preferred-size: 0;
  flex-basis: 0;
  -ms-flex-positive: 1;
  flex-grow: 1;
  max-width: 100%;
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}

.w-100 {
  width: 100% !important;
}
.d-block {
  display: block !important;
}
.img-thumbnail {
  padding: 0.25rem;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  max-width: 100%;
  height: auto;
}
img {
  vertical-align: middle;
  border-style: none;
}
</style>
