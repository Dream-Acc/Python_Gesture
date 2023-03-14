<template>
  <div class="task">
    <div class="task-top">
      <div class="task-name">
        <p class="task-name-content">{{ this.taskName }}</p>
      </div>
    </div>
    <div class="task-start" @click="changePage">
      <span>去学习</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Task",
  props: {
    taskName: {
      type: String,
      default: "单词",
    },
  },
  data() {
    return {
      linkPage: "",
    };
  },
  methods: {
    findLink() {
      if (this.taskName === "单词") {
        this.linkPage = "/words";
      } else if (this.taskName === "测试") {
        this.linkPage = "/test";
      } else if (this.taskName === "生词") {
        this.linkPage = "/unfamiliar";
      }
    },
    changePage() {
      this.findLink();
      this.$router.push(this.linkPage);
    },
  },
};
</script>

<style scoped>
.task {
  flex: 1;
  margin: 1em 1em;
  height: 270px;
  cursor: pointer;
  background-color: white;
  border-radius: 5px;
  box-shadow: #ccc 2px 2px 8px;
}
p {
  font-size: 35px;
  margin: 0 0 10px;
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}
.task,
.task-top,
.task-name {
  text-align: center;
}
span {
  line-height: 162px;
  color: #7c8a8a;
  font-size: 20px;
}
.task-start {
  background-color: #f0f0f0;
}
</style>
