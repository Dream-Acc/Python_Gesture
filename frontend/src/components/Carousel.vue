<template>
  <div class="block">
    <el-carousel :height="bannerHeight + 'px'" loop>
      <el-carousel-item v-for="item in imageList" :key="item">
        <span>内容</span>
        <img
          :src="item"
          class="rightImg"
          alt="轮播图无法打开"
          referrerpolicy="no-referrer"
        />
        <span>生动有趣</span>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Carousel",
  props: {
    imageList: {
      type: [],
      default: [
        "https://www.maimemo.com/res/images/site/home/section2.png",
        "https://www.maimemo.com/res/images/site/home/section3.png",
        "https://www.maimemo.com/res/images/site/home/section4.png",
      ],
    },
  },
  data() {
    return {
      images: [],
      imgList: [],
      // 图片父容器高度
      bannerHeight: 1000,
      // 浏览器宽度
      screenWidth: 0,
    };
  },
  methods: {
    setSize: function () {
      // 通过浏览器宽度(图片宽度)计算高度
      this.bannerHeight = (300 / 1550) * this.screenWidth;
    },
  },
  mounted() {
    // 首次加载时,需要调用一次
    this.screenWidth = window.innerWidth;
    this.setSize();
    // 窗口大小发生改变时,调用一次
    window.onresize = () => {
      this.screenWidth = window.innerWidth;
      this.setSize();
    };
  },
};
</script>
<style scoped>
el-carousel {
  background-color: #209e85;
}
el-carousel-item {
  color: #fff;
  background-color: #209e85;
  margin: 0;
}
.rightImg {
  height: inherit;
}
span {
  margin: 0 20px;
  font-size: 30px;
}
</style>
