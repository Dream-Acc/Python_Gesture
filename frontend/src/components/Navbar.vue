<template>
  <div class="nav">
    <nav>
      <div class="logo">
        <img src="../asset/icon.png" alt="我是一个图标" class="icon" />
        <img src="../asset/menu.png" alt="我是一段介绍" class="menu" />
      </div>
      <div class="el-menu-item" @click="toHome">首页</div>
      <div class="el-menu-item" @click="toWord">单词</div>
      <div class="el-menu-item" @click="toTest">测试</div>
      <div class="el-menu-item" @click="toUnfamiliar">生词</div>
      <div class="el-menu-item" @click="toIntroduce">手语课堂</div>
      <div class="el-menu-item" @click="toUs">关于我们</div>
      <div
        class="el-menu-item"
        id="log-in"
        @click="toLogIn"
        v-if="!this.$store.getters.getUserName"
      >
        登录/注册
      </div>
      <div class="el-menu-item" v-if="this.$store.getters.getUserName">
        您好! {{ this.$store.getters.getUserName }}
      </div>
      <div
        class="el-menu-item"
        @click="logOut"
        v-if="this.$store.getters.getUserName"
      >
        退出登录
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  name: "Navbar",
  data() {
    return {
      linkPage: "",
      notLogin: true,
    };
  },
  methods: {
    toHome() {
      this.linkPage = "/home";
      this.$router.push(this.linkPage);
    },
    toWord() {
      this.linkPage = "/words";
      this.$router.push(this.linkPage);
    },
    toTest() {
      this.linkPage = "/test";
      this.$router.push(this.linkPage);
    },
    toUnfamiliar() {
      this.linkPage = "/unfamiliar";
      this.$router.push(this.linkPage).catch((err) => {
        this.$router.go(0);
      });
    },
    toIntroduce() {
      this.linkPage = "/Introduce";
      this.$router.push(this.linkPage).catch((err) => {
        this.$router.go(0);
      });
    },
    toLogIn() {
      this.linkPage = "/logIn";
      this.$router.push(this.linkPage);
    },
    toUs() {
      this.linkPage = "/AboutUs";
      this.$router.push(this.linkPage);
    },
    logOut() {
      this.$store.commit("setUserName", "");
      this.$message.success("您已成功退出登录！");
    },
  },
};
</script>

<style scoped>
nav {
  display: flex;
  align-items: center;
  justify-content: left;
  padding-left: 50px;
  background-color: #209e85;
}
.el-menu-item {
  color: white;
  padding: 0.5% 2%;
  text-align: center;
  border-bottom: transparent;
  display: flex;
  transition: 0.4s;
  font-size: larger;
  opacity: 0.9;
}
.el-menu-item:hover {
  background-color: #209e85;
  border-bottom: solid 4px;
  border-bottom-color: #3d7d86;
  height: 65px;
}
.logo {
  margin-right: 10px;
}
.menu {
  width: 40%;
  height: 40%;
  margin-right: 0px;
}
.icon {
  margin-left: 0px;
  width: 10%;
  height: 10%;
}
</style>
