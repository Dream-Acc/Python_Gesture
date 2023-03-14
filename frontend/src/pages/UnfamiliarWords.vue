<template>
  <div class="background">
    <div class="learn-word">
      <p v-if="visible" style="float;: left" class="total">
        共{{ this.words.length }}个生词（熟练度30以下）
      </p>
      <a-list
        :grid="{ gutter: 12, column: 2 }"
        :data-source="this.words"
        size="small"
        :pagination="pagination"
        v-if="visible"
      >
        <a-list-item
          slot="renderItem"
          slot-scope="item, index"
          style="float;: left"
          @click="showWord(item.description, item.title, item.path)"
        >
          <a-list-item-meta
            :description="item.description"
            :title="item.title"
          ></a-list-item-meta>
          <div class="progress">
            <div class="text">熟练度</div>
            <el-progress
              :text-inside="true"
              :stroke-width="15"
              :percentage="item.proficiency"
            ></el-progress>
          </div>
          <a-divider></a-divider>
        </a-list-item>
      </a-list>
      <div class="card" v-else>
        <el-page-header @back="goBack" content="词卡"></el-page-header>
        <a-divider></a-divider>
        <word-learning-card
          :title="currentTitle"
          :description="currentDescription"
          :path="currentPath"
          class="word-card"
        ></word-learning-card>
      </div>
    </div>
  </div>
</template>

<script>
import WordLearningCard from "../components/WordLearningCard.vue";
export default {
  components: { WordLearningCard },
  data() {
    return {
      words: [],
      pagination: {
        onChange: (page) => {
          console.log(page);
        },
        pageSize: 8,
      },
      visible: true,
      currentTitle: "",
      currentDescription: "",
      currentPath: "",
      username: this.$store.getters.getUserName,
    };
  },
  methods: {
    goBack() {
      this.visible = true;
    },
    showWord(description, title, path) {
      this.visible = false;
      this.currentTitle = title;
      this.currentDescription = description;
      this.currentPath = path;
    },
    getData() {
      let params = new URLSearchParams();
      params.append("username", this.username);
      this.$http.post("/display/gesture/send_words/", params).then((res) => {
        console.log(res);
        this.words = res.data;
        for (let i = 0; i < this.words.length; i++) {
          this.words[i].path = require("../demo_video/" +
            this.words[i].Eng +
            ".mp4");
        }
      });
    },
  },
  mounted: function () {
    if (this.$store.getters.getUserName == "") {
      this.$message.info("请先登录");
      this.$router.push("/logIn");
      return;
    }
    this.visible = true;
    this.getData();
  },
};
</script>

<style scoped>
.learn-word {
  margin-top: 10%;
}

.card {
  width: 50%;
  margin: auto;
}

.word-card {
  width: 100%;
  vertical-align: middle;
  margin: auto;
  /* margin-top: 10%; */
}

.total {
  width: 80%;
  text-align: right;
  font-size: 15px;
  line-height: 1.5;
  color: rgba(0, 0, 0, 0.85);
}

.ant-list {
  width: 60%;
  margin-left: 20%;
  margin-top: 2%;
}

.ant-list-item-meta-title {
  font-size: 18px;
  font-weight: 700;
  color: #333;
  flex-grow: 1;
  cursor: pointer;
  text-align: left;
}

.ant-list-item-meta-description {
  color: rgb(102, 102, 102);
  text-align: left;
}

.progress {
  margin-top: 10px;
}

.text {
  float: left;
  font-weight: bold;
}
</style>