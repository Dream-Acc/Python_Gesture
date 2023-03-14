<template>
  <div>
    <div class="top_blank">
      <Pic></Pic>
    </div>
    <el-main>
      <div class="tasks">
        <task task-name="单词"></task>
        <task task-name="生词"></task>
        <task task-name="测试"></task>
      </div>
      <div class="notes">
        <motivational-note></motivational-note>
      </div>
    </el-main>
    <FivePicture></FivePicture>
    <Footer></Footer>
  </div>
</template>

<script>
import Task from "../components/Task";
import MotivationalNote from "../components/MotivationalNote";
import Main from "../components/Main";
import Carousel from "../components/Carousel";
import Footer from "../components/Footer";
import FivePicture from "../components/FivePicture";
import Pic from "../components/Pic";
export default {
  name: "home",
  components: {
    FivePicture,
    Footer,
    Carousel,
    Main,
    MotivationalNote,
    Task,
    Pic,
  },
};
</script>

<style scoped>
.tasks {
  display: flex;
  height: auto;
}
.notes {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.top_blank {
  margin-top: 40px;
}
</style>
