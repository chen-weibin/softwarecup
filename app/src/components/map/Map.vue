<template>
    <div class="map">
        <div class="tip" v-show="tip">没有遥感图像，可从中截取图片进行解译
            <svg-icon iconClass='close' className='icon' @click.native="close"/>
        </div>
        <div class="allmap" id="allmap"></div>
        <div class="fh" @click="gotoUp">
            返回
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Map',
        data() {
            return {
                tip: true,
            }
        },
        mounted() {
            let map = new BMapGL.Map("allmap");    // 创建Map实例
            map.centerAndZoom(new BMapGL.Point(118.093741, 24.630037), 18);  // 初始化地图,设置中心点坐标和地图级别
            //map.centerAndZoom(new BMapGL.Point(118.093741,24.630037), -1);  // 初始化地图,设置中心点坐标和地图级别
            map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
            map.setMapType(BMAP_EARTH_MAP);
        },
        methods: {
            gotoUp() {
                this.$parent.map = false
            },
            close() {
                this.tip = false
            }
        }
    }
</script>

<style lang='less' scoped>
    .map {
        width: 100%;
        height: 100%;
        position: relative;
        .allmap {
            width: 100%;
            height: 100%;
            overflow: hidden;
            margin: 0;
            font-family: "微软雅黑";
            background-color: #fff;
        }
        .tip {
            position: absolute;
            top: -33px;
            right: 100px;
            font-size: 20px;
            z-index: 10;
            height: 30px;
            width: 420px;
            text-align: center;
            line-height: 30px;
            color: rgb(0, 0, 0);
            border-radius: 15px;
            background-color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-left: 17px;
            .icon {
                width: 25px !important;
                height: 25px !important;
                margin-right: 7px;
            }
        }
        .fh {
            position: absolute;
            top: -30px;
            right: 10px;
            font-size: 20px;
            z-index: 10;
            color: white;
            cursor: default;
            transition: all .5s;
            &:hover {
                transform: translateY(-2px);
            }
        }
        

    }
</style>