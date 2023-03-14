<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span style="float: left">{{ title }}</span>
        <el-button
          style="float: right; padding: 3px 0; border: none; font-size: 24px"
          icon="el-icon-thumb"
          @click="showModal"
        ></el-button>
      </div>
      <div class="description">
        <h5>动作解释</h5>
        <p>{{ description }}</p>
      </div>
      <h5>手势演示</h5>
      <video
        ref="mp4"
        :src="path"
        muted
        autoplay
        loop
        controls
        style="float: left"
        v-if="!visible"
      ></video>
    </el-card>
    <a-modal
      v-model="visible"
      title="手势练习"
      @ok="handleOk"
      :closeable="true"
      :footer="false"
      :maskStyle="{ animation: 'none', background: '#fff', opacity: '0.7' }"
    >
      <p>请模仿视频中的手势</p>
    </a-modal>
  </div>
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
      default: require("../asset/test.mp4"),
    },
  },
  data() {
    return {
      clickNum: 0,
      descriptionShow: false,
      videoShow: false,
      visible: false,
    };
  },
  methods: {
    forgetWord() {
      this.clickNum = this.clickNum + 1;
      switch (this.clickNum) {
        case 1:
          this.descriptionShow = true;
          break;
        case 2:
          // 展示视频信息
          this.videoShow = true;
          break;
      }
    },
    knownWord() {
      this.clickNum = 0;
      this.descriptionShow = false;
      this.videoShow = false;
      this.$emit("pass");
    },
    showModal() {
      this.visible = true;
      let params = new URLSearchParams();
      params.append("label", this.title);
      this.$http.post("/display/gesture/model_test/", params).then((res) => {
        console.log(res);
        if (res.data === "Success") {
          this.$message.success("匹配成功");
          this.visible = false;
        } else {
          this.$message.info("请继续练习");
        }
      });
    },
    handleOk(e) {
      console.log(e);
      this.visible = false;
    },
  },
  created: function () {
    this.$refs.mp4.load();
  },
};
</script>
<style scoped>
span {
  font-size: 35px;
  padding-left: 5%;
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
  text-align: left;
  width: 40%;
  object-fit: fill;
  margin-bottom: 5%;
  margin-top: 1%;
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
  color: #209e85;
  text-align: left;
  padding-left: 5px;
}

h5 {
  font-size: 14px;
  color: #b0b4be;
  padding-top: 10px;
  text-align: left;
  width: 80%;
  vertical-align: middle;
}
</style>