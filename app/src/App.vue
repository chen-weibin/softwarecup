<template>
  <div id="app">
    <keep-alive exclude="LoginFrame">
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
  export default {
    name: "App",
  };
</script>

<style>
  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }
  :root {
    --main-bg: white;
    --main-font-color: black;

    --bgc-start-color: #e4e4e4;
    --bgc-middle-color: #e4e4e4;
    --bgc-end-color: #e4e4e4;

    --theme-select-color: #fff;
    --theme-select-slider: #517fff;
    --theme-select-text-color: black;
    --theme-select-text-bg-color: rgb(241, 241, 241);

    --header-bg-color: #517fff;
    --max-min-screen: white;

    --title-color: white;

    --aside-bg-first-color: #7b9efe;
    --aside-bg-second-color: #7b9efe;
    --aside-bg-third-color: #7b9efe;
    --aside-bg-fourth-color: #7b9efe;
    --aside-mask-start-color: transparent;
    --aside-mask-end-color: transparent;

    --item-bg-color: #15CE96;

    --menu-now-font-color: rgb(255, 255, 255);
    --menu-now-bg-color: #08e09f;
    --menu-bg-color: #618bfe;
    --menu-font-color: white;
    --menu-message-bg-color: #FFFFFF;
    --menu-message-title-color: black;
    --menu-message-desc-color: black;
    --menu-message-dian-color: #08e09f;
    --menu-tools-bg-color: #08e09f;
    --menu-tools-font-color: rgb(255, 255, 255);
    --memu-border-color: transparent;

    --information-bg: white url('~@/assets/卫星.png') no-repeat 275px 245px;
    --information-title-color: black;
    --information-item-color: rgb(126, 125, 125);
    --information-desc-color: black;
    --information-one-color: rgb(107, 255, 122);
    --information-two-color: rgb(255, 51, 28);
    --information-three-color: rgb(251, 255, 0);
    --information-four-color: rgb(76, 210, 255);
    --information-five-color: rgb(255, 188, 54);

    --history-bg: white;
    --history-item-bg-color: #4de4b6;
    --history-item-before: black;
    --history-item-label: white;
    --history-item-time: black;
    --history-scroll-track: #cccccc;
    --history-scroll-thumb: #83a4ff;
    --history-scroll-hover: #7096ff;


    --change-bg: white url('~@/assets/卫星.png') no-repeat 160px -30px;
    --change-ra: none;
    --change-bt: #13dfa2;
    --change-tip-circle: #d7dbe1;
    --change-tip-line: #E4E7ED;
    --change-font: #4b4c4f;
    --change-res-border: none;

    --upload-border: #d9d9d9;
    --upload-border-hov: #7B9EFE;
    --upload-font: #606266;
    --upload-tit: #409eff;
    --upload-icon: #C0C4CC;

    --user-bg-border: #d1d1d1;
    --user-bg: rgb(254, 253, 254);
    --user-touxiang: rgb(68, 162, 255);
    --user-list-font: rgb(42, 42, 42);
    --user-show: #E3E5E7;

    --scan-color: #517FFF;
    --scan-line: rgb(0, 255, 166);
    --scan-show1: linear-gradient(to bottom, rgba(88, 255, 197, .0), rgba(88, 255, 197, .7));
    --scan-show2: linear-gradient(to top, rgba(88, 255, 197, .0), rgba(88, 255, 197, .7));


  }
  #app {
    width: 100wh;
    height: 100vh;
    overflow: hidden;
    background-image: linear-gradient(to right, var(--bgc-start-color), var(--bgc-middle-color),var(--bgc-end-color));
  }
  
  @keyframes toright {
      0% {
          opacity: 0;
          transform: translateX(-100%);
      }
      100% {
          opacity: 1;
          transform: translateX(0);
      }
  }

  @keyframes toleft {
      0% {
          opacity: 0;
          transform: translateX(100%);
      }
      100% {
          opacity: 1;
          transform: translateX(0);
      }
  }

  @keyframes tobottom {
      0% {
          opacity: 0;
          transform: translateY(-100%);
      }
      100% {
          opacity: 1;
          transform: translateY(0);
      }
  }

  @keyframes totop {
      0% {
          opacity: 0;
          transform: translateY(100%);
      }
      100% {
          opacity: 1;
          transform: translateY(0);
      }
  }

    .el-carousel__button {
      background-color: #517FFF !important; 
      /* #ff9203 */
  }


  @keyframes loadinging {
      0% {
          clip-path: polygon(
              0% 0%,
              0% 0%,
              0% 0%,
              0% 0%,
              0% 0%,
              50% 50%
          );
      }
      15% {
          clip-path: polygon(                
              0% 0%,
              100% 0%,
              100% 0%,
              100% 0%,
              100% 0%,
              50% 50%
          );
      }
      25% {
          clip-path: polygon(
              0% 0%,
              100% 0%,
              100% 100%,
              100% 100%,
              100% 100%,
              50% 50%
          );
      }
      43% {
          clip-path: polygon(
              0% 0%,
              100% 0%,
              100% 100%,
              0% 100%,
              0% 100%,
              50% 50%
          );
      }
      50% {
          clip-path: polygon(
              0% 0%,
              100% 0%,
              100% 100%,
              0% 100%,
              0% 50%,
              50% 50%
          );
      }       
      65% {
          clip-path: polygon(
              100% 0%,
              100% 0%,
              100% 100%,
              0% 100%,
              0% 50%,
              50% 50%
          );
      }
      75% {
          clip-path: polygon(
              100% 100%,
              100% 100%,
              100% 100%,
              0% 100%,
              0% 50%,
              50% 50%
          );
      }
      95% {
          clip-path: polygon(
              0% 100%,
              0% 100%,
              0% 100%,
              0% 100%,
              0% 50%,
              50% 50%
          );
      }
      100% {
          clip-path: polygon(
              0% 80%,
              0% 80%,
              0% 80%,
              0% 80%,
              0% 50%,
              50% 50%
          );
      }
  }
    .BMap_cpyCtrl span {
        display: none !important;
    }
    @keyframes rotateing {
        0% {
            transform: rotate(0);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>
