<template>
  <div class="login-register">
    <div class="contain">
      <div class="big-box" :class="{ active: isLogin }">
        <div class="big-contain" key="bigContainLogin" v-if="isLogin">
          <div class="big-title">账户登录</div>
          <div class="big-form">
            <input type="email" placeholder="用户名" v-model="form.username" />
            <input
              type="password"
              placeholder="密码"
              v-model="form.password"
              @keyup.enter="login"
              ref="login"
            />
          </div>
          <button class="big-button" @click="login">登录</button>
        </div>
        <div class="big-contain" key="bigContainRegister" v-else>
          <div class="big-title">创建账户</div>
          <div class="big-form">
            <input type="text" placeholder="用户名" v-model="form.username" />
            <input
              type="password"
              placeholder="密码"
              v-model="form.password"
              @keyup.enter="register"
            />
          </div>
          <button class="big-button" @click="register">注册</button>
        </div>
      </div>
      <div class="small-box" :class="{ active: isLogin }">
        <div class="small-contain" key="smallContainRegister" v-if="isLogin">
          <div class="small-title">还是陌生人？</div>
          <p class="small-content">开始注册，加入手语学习的旅行</p>
          <button class="small-button" @click="changeType">注册</button>
        </div>
        <div class="small-contain" key="smallContainLogin" v-else>
          <div class="small-title">已有账号？</div>
          <p class="small-content">登录账号，继续你的旅行</p>
          <button class="small-button" @click="changeType">登录</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login-register",
  data() {
    return {
      isLogin: false,
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    changeType() {
      this.isLogin = !this.isLogin;
      this.form.username = "";
      this.form.password = "";
    },
    login() {
      let params = new URLSearchParams();
      params.append("username", this.form.username);
      params.append("password", this.form.password);
      this.$http.post("/display/gesture/login_test/", params).then((res) => {
        console.log(res);
        if (res.data === "login success") {
          this.$store.commit("setUserName", this.form.username);
          this.$message.success(
            "登录成功,当前用户为：" + this.$store.getters.getUserName
          );
          this.$router.push("/home");
        } else {
          this.$message.error("登录失败");
        }
      });
    },
    register() {
      let params = new URLSearchParams();
      params.append("username", this.form.username);
      params.append("password", this.form.password);
      this.$http.post("/display/gesture/register_test/", params).then((res) => {
        console.log(res);
        if (res.data === "register success") {
          this.$message.success("注册成功");
        } else if (res.data === "user exist") {
          this.$message.error("已注册的账号");
          this.isLogin = !this.isLogin;
          this.$refs.login.focus();
        } else {
          this.$message.info("请保证密码长度超过8位且包含数字和字母");
        }
      });
    },
  },
};
</script>

<style scoped="scoped">
.login-register {
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
}

.contain {
  width: 60%;
  height: 60%;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 3px #f0f0f0, 0 0 6px #f0f0f0;
}

.big-box {
  width: 70%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 30%;
  transform: translateX(0%);
  transition: all 1s;
}

.big-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.big-title {
  font-size: 1.5em;
  font-weight: bold;
  color: #209e85;
}

.big-form {
  width: 100%;
  height: 40%;
  padding: 2em 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.big-form .errTips {
  display: block;
  width: 50%;
  text-align: left;
  color: red;
  font-size: 0.7em;
  margin-left: 1em;
}

.big-form input {
  width: 50%;
  height: 30px;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em;
  background-color: #f0f0f0;
}

.big-button {
  width: 20%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: #209e85;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.small-box {
  width: 30%;
  height: 100%;
  background: linear-gradient(135deg, #209e85, #c4e0e5);
  position: absolute;
  top: 0;
  left: 0;
  transform: translateX(0%);
  transition: all 1s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
}

.small-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.small-title {
  font-size: 1.5em;
  font-weight: bold;
  color: #fff;
}

.small-content {
  font-size: 0.8em;
  color: #fff;
  text-align: center;
  padding: 2em 4em;
  line-height: 1.7em;
}

.small-button {
  width: 60%;
  height: 40px;
  border-radius: 24px;
  border: 1px solid #fff;
  outline: none;
  background-color: transparent;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.big-box.active {
  left: 0;
  transition: all 0.5s;
}

.small-box.active {
  left: 100%;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  transform: translateX(-100%);
  transition: all 1s;
}
</style>
