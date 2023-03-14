<template>
  <div>
    <!-- 图文巨幕 -->
    <div class="bigp back">
      <h1 class="head1 mar-pic">手语课堂</h1>
      <p class="lead p1-pic mar-pic">手之声，让我们一起学会聆听手的声音</p>
      <hr class="my-4 mar-pic line" />
      <img class="pic1" src="../asset/introduct/2(1).png" />
    </div>

    <!-- 手语发展 -->
    <div class="main pic ld_library">
      <div class="block news-wrap">
        <div class="content news">
          <div class="sub-title">
            <h2>手语发展</h2>
            <h3>DEVELOPMENT</h3>

            <div class="yellow-rectangle"></div>
          </div>
          <div class="card-wrap">
            <div class="img-wrap img-shadow1">
              <a>
                <img src="../asset/introduct/develop.jpg" />
              </a>
            </div>
            <div class="list" @click="changeToHistory">
              <a>
                <p class="title g-ellipsis p1">20世纪50年代~1988年</p>
                <p class="p1">
                  手语是聋人表达思想、进行交际的工具。由于我国地域辽阔，存在众多的地方手语，给聋人之间交流带来了不便。确定规范……
                </p>
              </a>
              <hr class="city-hr" />
              <a>
                <p class="title g-ellipsis p1">1988年~2001年</p>
                <p class="p1">
                  1988年，中国残联成立以后又组织专家在原有手语研究的基础上，结合有声语言和手指语的使用，编辑出版了统一规范的……
                </p>
              </a>
              <hr class="city-hr" />
              <a>
                <p class="title g-ellipsis p1">2001年~至今</p>
                <p class="p1">
                  修订《中国手语》。为适应新形势需要，中国残联教育就业部和中国聋人协会于2001年7月，共同委托北京师范大学特殊教……
                </p>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 手语种类 -->
    <div class="block city-wrap ld_library back1">
      <div class="content city">
        <div class="sub-title">
          <h2>手语种类</h2>
          <h3>TYPE</h3>

          <div class="yellow-rectangle"></div>
        </div>
        <div class="card-list">
          <div class="card1 img-shadow1" @click="changePage(1)">
            <a @click="changeToType1">
              <div class="img-wrap1">
                <img class="img1" src="../asset/introduct/t_1.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">中国手语</h3>
              <p class="title g-ellipsis p2">协会负责 手语推广 交际表达</p>
              <p class="p2">
                1995年，国务院"定职能、定机构、定编制"方案明确了中国残联负责研究、推广手语的职能。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis" @click="changeToType1">手语来源</a>
              <a class="item g-ellipsis" @click="changeToType1">手语特点</a>
              <a class="item g-ellipsis" @click="changeToType1">发展过程</a>
              <a class="item g-ellipsis" @click="changeToType1">适用人群</a>
            </div>
          </div>
          <div class="card1 img-shadow1" @click="changePage()">
            <a @click="changeToType2">
              <div class="img-wrap1">
                <img class="img1" src="../asset/introduct/t_2.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">指唇语</h3>
              <p class="title g-ellipsis p2">手口并用 声(介)母+唇型</p>
              <p class="p2">
                《指唇语》，它是用右手声母和唇型韵母(或附加左手韵母)来辅助汉语口语教学的一种手语方案。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis" @click="changeToType2">手语来源</a>
              <a class="item g-ellipsis" @click="changeToType2">手语特点</a>
              <a class="item g-ellipsis" @click="changeToType2">发展过程</a>
              <a class="item g-ellipsis" @click="changeToType2">适用人群</a>
            </div>
          </div>
          <div class="card1 img-shadow1" @click="changePage()">
            <a @click="changeToType3">
              <div class="img-wrap1">
                <img class="img1" src="../asset/introduct/t_3.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">特警手语</h3>
              <p class="title g-ellipsis p2">方正规范 简单易懂</p>
              <p class="p2">
                特警队员执行任务时的动作统称为特警手语，它是特警队员们互相交流、沟通和协作的重要桥梁。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis" @click="changeToType3">手语来源</a>
              <a class="item g-ellipsis" @click="changeToType3">手语特点</a>
              <a class="item g-ellipsis" @click="changeToType3">发展过程</a>
              <a class="item g-ellipsis" @click="changeToType3">适用人群</a>
            </div>
          </div>
          <div class="card1 img-shadow1" @click="changePage(4)">
            <a @click="changeToType4">
              <div class="img-wrap1">
                <img class="img1" src="../asset/introduct/t_4.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">双拼掌语</h3>
              <p class="title g-ellipsis p2">屋角掌语 直伸程度 手臂幅度</p>
              <p class="p2">
                相比指语拼音，双拼掌语两次手语动作表达一个字音，字母动作清楚，有效交流距离更远。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis" @click="changeToType4">手语来源</a>
              <a class="item g-ellipsis" @click="changeToType4">手语特点</a>
              <a class="item g-ellipsis" @click="changeToType4">发展过程</a>
              <a class="item g-ellipsis" @click="changeToType4">适用人群</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 5张图 -->
    <!-- introduction -->
    <div class="introduction ld_library">
      <h2>手语特性</h2>
      <h3>CHARACTERISTIC</h3>

      <div class="yellow-rectangle"></div>
      <div class="introduction_main">
        <ul class="introduction_ul">
          <li>
            <div class="introduction_div">
              <a @click="changeToCharacter1"
                ><img
                  class="introduction_picture"
                  src="../asset/introduct/c_1.jpg"
                  alt="无法显示"
                  title="图片1"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span1"
                ><p class="introduction_p">
                  社团性。手势语实际上是听障人和语言障碍者的"民族言语"――社团语言，他们对手势语怀有深厚的感情。
                </p>
              </span>
            </div>
          </li>
          <li>
            <div class="introduction_div">
              <a @click="changeToCharacter2"
                ><img
                  class="introduction_picture"
                  src="../asset/introduct/c_2.jpg"
                  alt="无法显示"
                  title="图片2"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span2"
                ><p class="introduction_p">
                  社会性。手语是随着社会的发展而发展的。手语由劳动产生，是在社会发展的基础上产生，随语言一起成长。
                </p>
              </span>
            </div>
          </li>
          <li>
            <div class="introduction_div">
              <a @click="changeToCharacter3"
                ><img
                  class="introduction_picture"
                  src="../asset/introduct/c_3.jpg"
                  alt="无法显示"
                  title="图片3"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span3"
                ><p class="introduction_p">
                  实用性。手语是听障人和语言障碍者的交际工具，这是任何人都知道的。手语和摩尔所说的"姿势语言"不同。
                </p>
              </span>
            </div>
          </li>
          <li class="introduction_li">
            <div class="introduction_div">
              <a @click="changeToCharacter4"
                ><img
                  class="introduction_picture"
                  src="../asset/introduct/c_4.jpg"
                  alt="无法显示"
                  title="图片4"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span4"
                ><p class="introduction_p">
                  规律性。手势和人类社会一起产生的，而把手势作为一种语言，它的产生和发展是则和聋人教育同步的。
                </p>
              </span>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <Footer></Footer>
    <footer></footer>
  </div>
</template>

<script>
import Footer from "../components/Footer";
export default {
  components: { Footer },
  methods: {
    changeToHistory() {
      this.$router.push("/history");
    },
    changeToType1() {
      this.$router.push("/Type1");
    },
    changeToType2() {
      this.$router.push("/Type2");
    },
    changeToType3() {
      this.$router.push("/Type3");
    },
    changeToType4() {
      this.$router.push("/Type4");
    },
    changeToCharacter1() {
      this.$router.push("/Character1");
    },
    changeToCharacter2() {
      this.$router.push("/Character2");
    },
    changeToCharacter3() {
      this.$router.push("/Character3");
    },
    changeToCharacter4() {
      this.$router.push("/Character4");
    },
  },
};
</script>

<style scoped>
/* 图文巨幕 */

.pic {
  left: 0;
  bottom: 0;
  opacity: 1;
}

.pic1 {
  left: 0;
  bottom: 0;
  opacity: 2;
  margin-left: 700px;
}
.bigp {
  height: 688px;
}

.head1 {
  padding-top: 190px;
  font-size: 48px;
  color: rgba(255, 255, 255, 0.85);
}

.p1-pic {
  margin-top: 20px;
  color: #4f4f4f;
}

.p2-pic {
  margin-bottom: 55px;
}

.mar-pic {
  text-align: center;
}

.back {
  text-align: left;
  background-image: url(../asset/introduct/1.jpg);
}

.line {
  width: 400px;
  color: #474747;
}

/*手语发展*/
h2 {
  font-size: 36px;
  font-weight: 600;
  color: #343434;
}

h3 {
  font-size: 14px;
  font-weight: 300;
  color: #8e8d8d;
  margin: 10px;
  line-height: 2;
}

.img-wrap {
  height: 423px;
}

.main {
  color: #330;
  /*background: #f7f6f8;*/
  min-width: 1200px;
  position: relative;
}
.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

.img-shadow1 {
  box-shadow: #959ea5 0px 0px 20px;
}

.pic {
  padding-top: 70px;
}

.sub-title {
  text-align: center;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

.news img {
  width: 751px;
  height: 423px;
  position: absolute;
  top: 0;
  left: 0;
}

.news .list {
  position: absolute;
  top: 0;
  right: 0;
  width: 449px;
}

.news .list a {
  position: relative;
  display: block;
  height: 141px;
  font-size: 14px;
  line-height: 21px;
  color: #8e8d8d;
  padding: 27px;
  box-sizing: border-box;
  transition: 0.3s;
  text-decoration: none;
}

.news {
  height: 628px;
}

.content {
  width: 1200px;
  position: relative;
  margin: 0 auto;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

a {
  text-decoration: none;
}

.news .list {
  position: absolute;
  top: 0;
  right: 0;
  width: 449px;
}

.news .list .title {
  font-size: 24px;
  font-weight: 400;
  color: #343434;
  line-height: 30px;
  margin-bottom: 14px;
  margin-top: 0;
}

.g-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.p1 {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}

.list a:hover p {
  color: #209e85;
}

.city-hr {
  margin: 0;
}

body,
td,
th {
  font: 14px -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Ubuntu,
    Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei UI, Microsoft YaHei, Source Han Sans CN, sans-serif;
}

h3,
li,
ol,
p,
ul {
  list-style: none;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
ul {
  margin: 0;
  padding: 0;
}

.yellow-rectangle {
  width: 40px;
  height: 9px;
  background: #209e85;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 30px;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

/* 手语种类 */
.city {
  height: 668px;
}

.content {
  width: 1200px;
  position: relative;
  margin: 0 auto;
}

.back1 {
  background: #f7f7f7;
}

.city .sub-title {
  padding-top: 50px;
  margin-bottom: 20px;
}

.sub-title[data-v-6f74154e] {
  text-align: center;
}

.city .card-list {
  margin-left: -43px;
}

.card1 {
  width: 266px;
  height: 416px;
  background: #fff;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
  display: inline-block;
  margin-left: 40px;
  margin-bottom: 35px;
  vertical-align: top;
  font-size: 14px;
  color: #8e8d8d;
  line-height: 21px;
  position: relative;
}

.img-wrap1 {
  width: 266px;
  height: 152px;
  overflow: hidden;
}

.img1 {
  width: 265px;
  height: 150px;
  vertical-align: middle;
  border: 0px;
}

.p2 {
  color: #8e8d8d;
  margin: 0 23px 7px;
}

.item-list {
  margin-left: -10px;
  position: absolute;
  bottom: 9px;
  width: 270px;
}

.item {
  width: 93px;
  line-height: 29px;
  padding: 0 5px;
  text-align: center;
  border-radius: 15px;
  color: #8e8d8d;
  display: inline-block;
  border: 1px solid #8e8d8d;
  margin-left: 16px;
  margin-bottom: 11px;
}

.h3-1 {
  font-size: 24px;
  line-height: 25px;
  font-weight: 300;
  margin: 21px 23px 7px;
  color: #000;
}

.item:hover {
  width: 95px;
  line-height: 31px;
  background: #209e85;
  color: #fff !important;
  border: none;
  text-decoration: none;
}

.card1 a:hover {
  color: gray;
}

.card1 a:hover h3 {
  color: #209e85;
}

.introduction {
  width: 100%;
  padding-top: 80px;
  padding-bottom: 100px;
}

.introduction_main {
  width: 1000px;
  margin: 0px auto 0px;
}

.introduction_ul {
  width: 1000px;
  overflow: hidden;
  padding-left: 0;
  margin-top: 0;
  margin-bottom: 0;
}

.introduction_ul li {
  list-style: none;
  width: 230px;
  float: left;
  margin-right: 26px;
}

.introduction_div {
  width: 230px;
  height: 165px;
  border: 1px solid gray;
}

.introduction_picture {
  width: 220px;
  height: 155px;
  padding-left: 1px;
  padding-right: 1px;
  padding-top: 4px;
  padding-bottom: 2px;
  vertical-align: top;
}

.introduction_text {
  width: 230px;
  margin-top: 10px;
}

.introduction_ul .introduction_li {
  list-style: none;
  width: 230px;
  float: left;
  margin-right: 0px;
}

input {
  overflow: visible;
}
</style>
