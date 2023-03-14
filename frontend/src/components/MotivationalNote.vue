<template>
  <div class="note">
    <div class="quote">
      <p>
        "It's the time you spent on your rose that makes your rose so
        important."
        <br />
        "正因为你为玫瑰花费了时间，它才变得如此重要。"
      </p>
      <small> "—— Antoine de Saint-Exupéry" </small>
    </div>
  </div>
</template>

<script>
export default {
  name: "MotivationalNote",
};
</script>

<style scoped>
.note {
  margin-top: 2em;
  padding: 20px;
  margin-bottom: 10px;
  background-color: #fff;
  border-radius: 5px;
  -webkit-box-shadow: #ccc 2px 2px 8px;
  box-shadow: #ccc 2px 2px 8px;
  border: none;
  min-width: 60%;
}
.quote {
  padding-bottom: 20px;
}
p {
  margin: 0 0 10px;
  font-size: 17.5px;
  font-weight: 300;
  line-height: 1.25;
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}
small {
  display: block;
  line-height: 20px;
  font-size: 16px;
  color: #209e85;
  float: right;
  font-weight: 300;
}
</style>
