<template>
    <div class="aside">
        <div class="item" @click="goto(1)">
            <div class="logo">
                <svg-icon iconClass="targetExtraction" className="icon"/>
            </div>
            <div class="right">
                <div class="title">目标提取</div>
                <div class="english">target extraction</div>
            </div>
            <div class="desc">卫星图像中指定对象的分割</div>
        </div>
        <div class="item" @click="goto(2)">          
            <div class="logo">
                <svg-icon iconClass="changeDetection" className="icon"/>
            </div>
            <div class="right">
                <div class="title">变化检测</div>
                <div class="english">change detection</div>
            </div>
            <div class="desc">同区域两个时期的卫星图像变化情况的分析</div>
        </div>
        <div class="item" @click="goto(3)">             
            <div class="logo">
                <svg-icon iconClass="targetDetection" className="icon"/>
            </div>
            <div class="right">
                <div class="title">目标检测</div>
                <div class="english">target detection</div>
            </div>
            <div class="desc">卫星图像中指定对象的检测</div>
        </div>
        <div class="item" @click="goto(4)">
            <div class="logo">
                <svg-icon iconClass="classification" className="icon"/>
            </div>
            <div class="right">
                <div class="title">地物分类</div>
                <div class="english">terrain classification</div>
            </div>
            <div class="desc">卫星图像每个像素的分类</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Aside',
        methods: {
            goto(index){
                this.$parent.isshow = false
                switch(index){
                    case 1:
                        const timer1 = setTimeout(() => {
                            this.$router.push({path: '/targetextraction'})
                            clearTimeout(timer1)
                        }, 800)
                        break
                    case 2:
                        const timer2 = setTimeout(() => {
                            this.$router.push({path: '/changedetection'})
                            clearTimeout(timer2)
                        }, 800)
                        break
                    case 3:
                        const timer3 = setTimeout(() => {
                            this.$router.push({path: '/targetdetection'})
                            clearTimeout(timer3)
                        }, 800)
                        break
                    case 4:
                        const timer4 = setTimeout(() => {
                            this.$router.push({path: '/classification'})
                            clearTimeout(timer4)
                        }, 800)
                        break
                }
            }
        }
    }
</script>

<style lang='less' scoped>
    .aside {
        width: 1100px;
        height: 28%;
        display: flex;
        align-items: center;
        padding: 0 30px;
    }
    .item {
        width: 210px;
        height: 100px;
        border-radius: 5px;
        margin: 0 25px;
        position: relative;
        overflow: hidden;
        color: white;
        transition: all .5s;
        cursor: pointer;
        &:hover {
            transform: translateY(-3px);
            box-shadow: 10px 10px 20px rgba(51, 51, 51, .5);
        }
        &::before{
            display: block;
            position: absolute;
            width: 100%;
            height: 100%;
            content: '';
            background: -webkit-radial-gradient(center top, 80px 200px, var(--aside-mask-start-color), var(--aside-mask-end-color));
        }
        &:nth-child(1){
            background-color: var(--aside-bg-first-color);           
        }
        &:nth-child(2){
            background-color: var(--aside-bg-second-color);
        }
        &:nth-child(3){
            background-color: var(--aside-bg-third-color);
        }
        &:nth-child(4){
            background-color: var(--aside-bg-fourth-color);
        }

        .logo {
            position: absolute;
            left: 20px;
            top: 20px;
            display: flex;
            align-content: center;
            justify-content: center;
            .icon {
                width: 40px !important;
                height: 40px !important;
                color: white;
            }

        }
        .right {
            position: absolute;
            width: calc(100% - 60px);
            height: calc(20px + 40px);
            left: 70px;
            .title {
                padding-top: 10px;
                font-size: 19px;
            }
            .english {
                position: absolute;
                left: 0;
                bottom: 0;
                padding: 0 0.5px;
                background-color: var(--item-bg-color);
                border-radius: 3px;
                font-size: 14.5px;
            }

        }
        .desc {
            position: absolute;
            left: 22px; 
            top: 66px;
            font-size: 13px;
        }
    }

</style>