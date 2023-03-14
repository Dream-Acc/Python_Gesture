<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>{{ title }}</span>
      <el-button
        style="float: right; padding: 3px 0; border: none; font-size: 24px"
        icon="el-icon-right"
        @click="passWord"
      ></el-button>
    </div>
    <div class="description" v-if="descriptionShow">
      <p>{{ description }}</p>
    </div>
    <video :src="path" muted autoplay loop controls v-if="videoShow"></video>
    <div class="button" v-if="!videoShow">
      <button @click="knownWord"><i class="el-icon-check"></i>熟识</button>
      <button @click="forgetWord">
        <i :class="this.icon"></i>{{ this.content }}
      </button>
    </div>
  </el-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: "错误",
    },
    description: {
      type: String,
      default: "无描述信息",
    },
    path: {
      type: String,
      default: "../asset/test.mp4",
    },
  },
  data() {
    return {
      clickNum: 0,
      descriptionShow: false,
      videoShow: false,
      content: "忘记",
      icon: "el-icon-close",
    };
  },
  methods: {
    forgetWord() {
      this.clickNum = this.clickNum + 1;
      switch (this.clickNum) {
        case 1:
          this.change_proficiency("-");
          this.content = "播放视频";
          this.icon = "el-icon-video-play";
          this.descriptionShow = true;
          break;
        case 2:
          // 展示视频信息
          this.videoShow = true;
          break;
      }
    },
    passWord() {
      this.clickNum = 0;
      this.descriptionShow = false;
      this.videoShow = false;
      this.content = "忘记";
      this.icon = "el-icon-close";
      this.$emit("pass");
    },
    knownWord() {
      this.clickNum = 0;
      this.descriptionShow = false;
      this.videoShow = false;
      this.content = "忘记";
      this.icon = "el-icon-close";
      this.change_proficiency("+");
      this.$emit("pass");
    },
    change_proficiency(signal) {
      let params = new URLSearchParams();
      params.append("username", this.$store.getters.getUserName);
      params.append("label", this.title);
      params.append("score", signal);
      this.$http
        .post("/display/gesture/proficiency_test/", params)
        .then((res) => {
          console.log(res.data);
        });
    },
  },
  mounted: function () {
    if (this.$store.getters.getUserName == "") {
      this.$message.info("请先登录");
      this.$router.push("/logIn");
    }
  },
};
</script>

<style scoped>
span {
  font-size: 35px;
}

.button button {
  width: 80%;
  background-color: #fff;
  border: 1px solid #ddd;
  font-size: 15px;
  min-height: 55px;
  text-align: left;
}

.button button:hover {
  background-color: #209e85;
  color: #fff;
}

i {
  margin-right: 10px;
}

video {
  width: 80%;
  object-fit: fill;
}

.el-button:hover {
  background: #fff;
  border-color: #fff;
  color: #209e85;
}

.el-button:active {
  background: #fff;
  border-color: #fff;
  color: #209e85;
}

.el-button:focus {
  background: #fff;
  border-color: #fff;
  color: #209e85;
}

p {
  min-height: 50px;
  vertical-align: middle;
  line-height: 50px;
  background-color: #ddd;
}
</style>
