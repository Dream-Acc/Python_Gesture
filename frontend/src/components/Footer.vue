<template>
  <footer class="footer slide-out slide-out--active">
    <div class="footer__main">
      <div>
        <nav class="footer__nav">
          <a href="https://git.code.tencent.com/Sobremesa/python_gesture">
            <h4 class="footer__nav-title">加入我们</h4>
          </a>
        </nav>
        <nav class="footer__nav">
          <h4 class="footer__nav-title" @click="showModal">联系我们</h4>
          <a-modal
            v-model:visible="visible"
            title="NKU软件工程Python小组"
            :footer="false"
          >
            <a-table :columns="columns" :data-source="data" :pagination="false">
              <a slot="name" slot-scope="text">{{ text }}</a>
              <template slot="title" slot-scope="currentPageData">
                先活着吧小组
              </template>
            </a-table>
          </a-modal>
        </nav>
      </div>
      <div class="logo__comment">
        <img class="footer__logo" src="../asset/icon.png" alt="logo" />
        <img
          src="../asset/footer.png"
          alt="这是一段文字"
          class="footer__comment"
        />
      </div>
    </div>
    <div class="footer__copyright">
      <p class="footer__copyright-left"></p>
      <p>2022 NKU软件工程Python小组——先活着吧课程设计</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      visible: false,
      columns: [
        {
          title: "姓名",
          dataIndex: "name",
          key: "name",
          scopedSlots: { customRender: "name" },
        },
        {
          title: "学号",
          dataIndex: "age",
          key: "age",
        },
        {
          title: "邮箱",
          dataIndex: "address",
          key: "address",
          ellipsis: false,
        },
      ],
      data: [
        {
          key: "1",
          name: "谢宇杭",
          age: 2013282,
          address: "2896450802@qq.com",
        },
        {
          key: "2",
          name: "李彦昊",
          age: 2012286,
          address: "1310724226@qq.com",
        },
        {
          key: "3",
          name: "陈子昂",
          age: 2012217,
          address: "1812432358@qq.com",
        },
        {
          key: "4",
          name: "陈世祺",
          age: 2012661,
          address: "2902529887@qq.com",
        },
        {
          key: "5",
          name: "侯智航",
          age: 2012829,
          address: "3325623194@qq.com",
        },
      ],
    };
  },
  methods: {
    showModal() {
      this.visible = true;
    },
    handleOk(e) {
      console.log(e);
      this.visible = false;
    },
  },
};
</script>

<style scoped>
.slide-out--active.footer {
  opacity: 1;
}

.slide-out.footer {
  -webkit-transition: opacity 1s ease-in-out 0.1s;
  -o-transition: opacity 1s ease-in-out 0.1s;
  transition: opacity 1s ease-in-out 0.1s;
}

.slide-out {
  will-change: transform, opacity;
}

.footer {
  padding-top: 56px;
  opacity: 0;
  background: #e3e3e3;
}

* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

footer {
  display: block;
}

.footer__main {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 80%;
  margin: 0 auto;
  padding-bottom: 32px;
}

.footer__nav {
  display: inline-block;
  margin-right: 56px;
}

.footer__nav-title {
  color: #666;
  font-weight: 300;
  line-height: 24px;
  cursor: pointer;
}

h1,
h2,
h3,
h4,
p {
  margin: 0;
}

.footer__nav-list {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  margin-top: 24px;
}

ol,
ul {
  margin: 0;
  padding: 0;
}

ul {
  list-style-type: none;
}

.footer__nav-item {
  color: #666;
  font-size: 12px;
  line-height: 24px;
}

a {
  color: #28bea0;
  text-decoration: none;
}

.footer__logo {
  width: 8%;
}

.footer__comment {
  width: 40%;
}

.logo__comment {
  display: flex;
  justify-content: flex-end;
}

img {
  max-width: 100%;
  border-style: none;
}

.footer__copyright {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 80%;
  margin: 0 auto;
  padding: 24px 0;
  color: #666;
  font-size: 12px;
  line-height: 20px;
  border-top: 1px solid #ccc;
}
</style>
