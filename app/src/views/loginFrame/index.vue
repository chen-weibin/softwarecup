<template>
    <div class="loginmain">
        <div class="map">
            <div class="jt"></div>
            <div class="lbx"></div>
        </div>
        <div class="loginjm">
            <Login />
        </div>
        <!-- <img class="img" src="../../assets/登陆背景.png" alt=""> -->
        <img class="img" src="../../assets/article/5.jpg" alt="">
    </div>
</template>

<script>
    import Login from '@/components/login'

    export default {
        name: 'LoginFrame',
        components: {
            Login
        }
    }
</script>

<style lang='less' scoped>
    .loginmain {
        width: 100%;
        height: 100%;
        position: relative;
        .img {
            width: 100%;
            height: 100%;
        }
    }
    
    .map {
        position: absolute;
        left: 26%;
        top: 50%;
        transform: translate(-50%, -50%);
        width: 518px;
        height: 518px;
        background: url('../../assets/map.png');
        .jt {
            position: absolute;
            left: 50%;
            top: 50%;
            width: 566px;
            height: 566px;
            transform: translate(-50%, -50%);
            background: url('../../assets/jt.png');
            animation: rotate3 10s linear infinite;
            z-index: 4;
        }
        .lbx {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 643px;
            height: 643px;
            opacity: .8;
            z-index: 2;
            background: url('../../assets/lbx.png');
            animation: rotate2 15s linear infinite;
        }
        @keyframes rotate2 {
            0% {
                transform: translate(-50%, -50%) rotate(0deg);  //定义旋转的初始化角度
            }
            100% {
                transform: translate(-50%, -50%) rotate(360deg);
            }
        }
        @keyframes rotate3 {
            0% {
                transform: translate(-50%, -50%) rotate(0deg);  //定义旋转的初始化角度
            }
            100% {
                transform: translate(-50%, -50%) rotate(-360deg);
            }
        }
    }
    .loginjm {
        position: absolute;
        left: calc(30% + 580px);
        top: 50%;
        transform: translate(-50%, -50%);
    }
</style>