<template>
  <div class="background">
    <div class="learn-word">
      <p v-if="visible" style="float;: left" class="total">
        共{{ this.data.length }}个词
      </p>
      <a-list
        :grid="{ gutter: 16, column: 2 }"
        :data-source="this.data"
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
            :path="item.path"
          >
          </a-list-item-meta>
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
      data: [],
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
      this.$http.post("/display/gesture/get_words/", params).then((res) => {
        console.log(res);
        this.data = res.data;
        for (let i = 0; i < this.data.length; i++) {
          this.data[i].path = require("../demo_video/" +
            this.data[i].Eng +
            ".mp4");
        }
      });
    },
  },
  mounted: function () {
    this.visible = true;
    this.getData();
  },
};
</script>

<style scoped>
.learn-word {
  margin-top: 8%;
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
</style>