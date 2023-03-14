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
  name: "Pic",
  props: {
    imageList: {
      type: [],
      default: [
        "http://mms0.baidu.com/it/u=142156856,1781678320&fm=253&app=120&f=JPEG&fmt=auto&q=75?w=1200&h=601",
        "http://mms0.baidu.com/it/u=2477093562,2451139966&fm=253&app=120&f=JPEG&fmt=auto&q=75?w=1200&h=586",
        "http://mms2.baidu.com/it/u=3016508931,203682589&fm=253&app=120&f=JPEG&fmt=auto&q=75?w=1200&h=617",
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
