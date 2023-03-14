<template>
  <div
    :class="isAnimation ? 'known' : 'learn-word'"
    @animationend="isAnimation = false"
  >
    <words-card
      :title="title"
      :description="description"
      :path="path"
      class="word-card"
      @pass="changeWord"
    ></words-card>
  </div>
</template>

<script>
import WordsCard from "../components/WordsCard.vue";
export default {
  components: { WordsCard },
  data() {
    return {
      title: "",
      description: "",
      path: "",
      isAnimation: false,
    };
  },
  methods: {
    changeWord() {
      this.isAnimation = true;
      let params = new URLSearchParams();
      params.append("label", this.title);
      this.$http.post("/display/gesture/word_test/", params).then((res) => {
        this.title = res.data.name;
        this.description = res.data.description;
        this.path = require("../demo_video/" + res.data.label + ".mp4");
      });
    },
  },
  created: function () {
    let params = new URLSearchParams();
    params.append("label", " ");
    this.$http.post("/display/gesture/word_test/", params).then((res) => {
      this.title = res.data.name;
      this.description = res.data.description;
      this.path = require("../demo_video/" + res.data.label + ".mp4");
    });
  },
};
</script>

<style>
.learn-word {
  text-align: center;
  vertical-align: middle;
  padding-bottom: 10%;
}

.word-card {
  width: 50%;
  vertical-align: middle;
  margin: auto;
  margin-top: 10%;
}

.known {
  text-align: center;
  vertical-align: middle;
  animation: move 1s;
}

@keyframes move {
  0% {
    transform: translateX(0%) rotate(0deg);
    opacity: 1;
  }

  50% {
    transform: translateX(-150%) rotate(-90deg);
    opacity: 0;
  }

  100% {
    transform: translateX(0%) rotate(0deg);
    opacity: 1;
  }
}
</style>

