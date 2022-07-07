<template>
    <div class="message">
        <div class="content">
            <div class="one">
                <img src="../../assets/article/2.jpg" alt="">
            </div>
            <div class="two">
                <img src="../../assets/article/1.png" alt="">
            </div>
            <div class="three">
                <img src="../../assets/article/3.jpg" alt="">
            </div>
            <div class="four">
                <img src="../../assets/article/4.png" alt="">
            </div>
        </div>
        <!-- <div class="left">
            <Chart />
        </div>
        <div class="right">
            <Information />
        </div> -->
    </div>
</template>

<script>
    // import Chart from './children/Chart.vue'
    // import Information from './children/Information.vue'
    export default {
        name: 'Message',
        // components: { 
        //     Chart,
        //     Information 
        // },
    }
</script>

<style lang='less' scoped>
    .message {
        width: 1100px;
        height: 72%;
        padding: 15px 45px 55px;
        // .left {
        //     float: left;
        //     width: 50%;
        //     height: 100%;
        //     border-radius: 8px;
        //     overflow: hidden;
        // }
        // .right {
        //     margin-left: 35px;
        //     float: right;
        //     width: calc(50% - 35px);
        //     height: 100%;
        //     border-radius: 8px;
        //     overflow: hidden;
        // }
    }
    .content {
        width: 100%;
        height: 100%;
        border-radius: 8px;
        overflow: hidden;
        position: relative;
        .one,
        .two,
        .three,
        .four {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            img{
                width: 100%;
                height: 100%;
            }
        }
        .two {
            animation: slidemove 10s linear infinite alternate;
        }
        .three {
            animation: hlmove 10s linear infinite alternate;
        }
        .four {
            animation: dlmove 10s linear infinite alternate;
        }
    }
    @keyframes slidemove {
        0% {
            clip-path: circle(0px at 0px 0px)
        }
        25% {
            clip-path: circle(1100px at 500px 0px)
        }
        50% {
            clip-path: circle(1100px at 500px 0px)
        }
        75% {
            clip-path: circle(1100px at 500px 0px)
        }
        100% {
            clip-path: circle(1100px at 500px 0px)
        }
    }
    @keyframes hlmove {
        0% {
            clip-path: circle(0px at 0px 200px)
        }
        25% {
            clip-path: circle(0px at 0px 200px)
        }
        50% {
            clip-path: circle(1300px at 0px 200px)
        }
        75% {
            clip-path: circle(1300px at 0px 200px)
        }
        100% {
            clip-path: circle(1300px at 0px 200px)
        }
    }
    @keyframes dlmove {
        0% {
            clip-path: circle(0px at 0px 0px)
        }
        25% {
            clip-path: circle(0px at 0px 0px)
        }
        50% {
            clip-path: circle(0px at 0px 0px)
        }
        75% {
            clip-path: circle(1100px at 500px 0px)
        }
        100% {
            clip-path: circle(1100px at 500px 0px)
        }
    }
</style>