import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: () => import("@/pages/Home")
    },
    {
      path: "/logIn",
      name: "Try",
      component: () => import("@/pages/Try")
    },
    {
      path: "/home",
      name: "Home",
      component: () => import("@/pages/Home")
    },
    {
      path: "/AboutUs",
      name: "AboutUs",
      component: () => import("@/pages/AboutUs")
    },
    {
      path: "/test",
      name: "test",
      component: () => import("@/pages/LearnWord")
    },
    {
      path: "/words",
      name: "words",
      component: () => import("@/pages/WordList")
    },
    {
      path: "/Introduce",
      name: "Introduce",
      component: () => import("@/pages/Introduce")
    },
    {
      path: "/history",
      name: "History",
      component: () => import("@/pages/History")
    },
    {
      path: "/unfamiliar",
      name: "unfamiliar",
      component: () => import("@/pages/UnfamiliarWords")
    },
    {
      path: "/Type1",
      name: "Type1",
      component: () => import("@/pages/Type1")
    },
    {
      path: "/Type2",
      name: "Type2",
      component: () => import("@/pages/Type2")
    },
    {
      path: "/Type3",
      name: "Type3",
      component: () => import("@/pages/Type3")
    },
    {
      path: "/Type4",
      name: "Type4",
      component: () => import("@/pages/Type4")
    },
    {
      path: "/Character1",
      name: "Character1",
      component: () => import("@/pages/Character1")
    },
    {
      path: "/Character2",
      name: "Character2",
      component: () => import("@/pages/Character2")
    },
    {
      path: "/Character3",
      name: "Character3",
      component: () => import("@/pages/Character3")
    },
    {
      path: "/Character4",
      name: "Character4",
      component: () => import("@/pages/Character4")
    },
    {
      path: "/FivePicture",
      name: "FivePicture",
      component: () => import("@/components/FivePicture")
    }
  ]
});
