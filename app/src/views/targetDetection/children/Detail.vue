<template>
    <div class="detaill">
        <div class="top">
            <div class="logolg">
                <img src="../../../assets/理工.png" alt="" class="lg">
            </div>
            <div class="title">
                |&nbsp;&nbsp;目标检测
            </div>
            <div class="returnbef">
                <span @click="returnHome">返回上一级</span>
            </div>
            <div class="returnhome">
                <span @click="returnMain">返回主页</span>
            </div>      
        </div>
        <div class="bottom">
            <div class="left">
                <div class="tit">上传示例</div>
                <div class="con">
                    <div class="item" v-for="(item, index) in showData" :key="index" :class="current === index ? 'current' : ''" @click="changeCurrent(index)">
                        <!-- <div class="time">dkfjkdfjk</div> -->
                        <div class="image">
                            <img :src="item.resimg1" alt="">
                        </div>
                        <div class="bot"></div>
                    </div>
                </div>
            </div>
            <div class="center">
                <img :src="openeyes ? showData[current].resimg2 : showData[current].resimg1" alt="">
            </div>
            <div class="right">
                <div class="con">
                    <div class="item">
                        <div class="one head">类别</div>
                        <div class="two head">描边</div>
                        <div class="three head">显示</div>
                    </div>
                    <div class="item">
                        <div class="one">操场</div>
                        <div class="two">
                            <div class="chaochang"></div>
                        </div>
                        <div class="three">
                            <div class="no" v-if="!showData[current].playground">未检测到</div>
                            <div class="isshow" @click="changeeyes" v-else>
                                <img src="../../../assets/eyes.svg" alt="" v-if="openeyes">
                                <img src="../../../assets/closeeyes.svg" alt="" v-else>
                            </div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="one">油桶</div>
                        <div class="two">
                            <div class="youguan"></div>
                        </div>
                        <div class="three">
                            <div class="no" v-if="!showData[current].oiltank">未检测到</div>
                            <div class="isshow" @click="changeeyes" v-else>
                                <img src="../../../assets/eyes.svg" alt="" v-if="openeyes">
                                <img src="../../../assets/closeeyes.svg" alt="" v-else>
                            </div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="one">飞机</div>
                        <div class="two">
                            <div class="feiji"></div>
                        </div>
                        <div class="three">
                            <div class="no" v-if="!showData[current].aircraft">未检测到</div>
                            <div class="isshow" @click="changeeyes" v-else>
                                <img src="../../../assets/eyes.svg" alt="" v-if="openeyes">
                                <img src="../../../assets/closeeyes.svg" alt="" v-else>
                            </div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="one">立交桥</div>
                        <div class="two">
                            <div class="lijiaoqiao"></div>
                        </div>
                        <div class="three">
                            <div class="no" v-if="!showData[current].overpass">未检测到</div>
                            <div class="isshow" @click="changeeyes" v-else>
                                <img src="../../../assets/eyes.svg" alt="" v-if="openeyes">
                                <img src="../../../assets/closeeyes.svg" alt="" v-else>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {TargetDetectionExample} from '@/api'
    export default {
        name: 'Detail',
        props: ['img', 'resimg', 'resdata'],
        data() {
            return {
                current: 0,
                openeyes: true,
                showData: []
            }
        },
        methods: {
            returnHome(){
                this.$parent.isDetail = false
            },
            returnMain() {
                this.$parent.isDetail = false
                this.$router.push({path: '/home'})
            },
            changeeyes() {
                this.openeyes = ! this.openeyes
            },
            changeCurrent(index) {
                this.current = index
            }
        },
        mounted(){
            TargetDetectionExample().then((res) => {
                const {data} = res.data
                for (let i = 0; i < data.length; i++) {
                    const temp = {
                        playground: false,
                        overpass: false,
                        oiltank: false,
                        aircraft: false,
                        resimg1: '',
                        resimg2: ''
                    }
                    if (data[i].playground.ishave) {
                        temp.playground = true
                        temp.resimg1 = data[i].playground.resimg1
                        temp.resimg2 = data[i].playground.resimg2
                    } else if (data[i].overpass.ishave){
                        temp.overpass = true
                        temp.resimg1 = data[i].overpass.resimg1
                        temp.resimg2 = data[i].overpass.resimg2
                    } else if (data[i].oiltank.ishave) {
                        temp.oiltank = true
                        temp.resimg1 = data[i].oiltank.resimg1
                        temp.resimg2 = data[i].oiltank.resimg2
                    } else if (data[i].aircraft.ishave) {
                        temp.aircraft =  true
                        temp.resimg1 = data[i].aircraft.resimg1
                        temp.resimg2 = data[i].aircraft.resimg2
                    }
                    this.showData.push(temp)          
                }
            }, error => {})
        },
        watch: {
            resimg: {
                immediate: true,
                handler() {
                    if (this.resimg) {
                        const temp = {
                            playground: this.resdata.playground.ishave,
                            overpass: this.resdata.overpass.ishave,
                            oiltank: this.resdata.oiltank.ishave,
                            aircraft: this.resdata.aircraft.ishave,
                            resimg1: this.img,
                            resimg2: this.resimg
                        }
                        const len = this.showData.length
                        if (len === 5) {
                            this.showData.unshift(temp)
                        } else {
                            this.showData[0] = temp
                        }
                    }
                }
            }
        },
    }
</script>

<style lang='less' scoped>
    .detaill {
        width: 100%;
        height: 100vh;
        position: absolute;
        left: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 9999;
        .bottom {
            width: 100%;
            height: calc(100% - 50px);
            position: relative;
        }
    }
    .top {
        width: 100%;
        height: 50px;
        background-color: #000000;
        .logolg {
            float: left;
            margin-left: 40px;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            .lg {
                width: 35px;
                height: 35px;
            }
        }
        .title {
            float: left;
            width: 125px;
            height: 50px;
            line-height: 50px;
            color: white;
            font-weight: 700;
            font-size: 21px;
            text-align: center;
        }
        .returnbef{
            float: right;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            span {
                height: 28px;
                width: 80px;
                font-weight: 700;
                color: white;
                line-height: 28px;
                text-align: center;
                margin-right: 30px;
                cursor: default;
            }
        }
        .returnhome{
            float: right;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            span {
                height: 28px;
                width: 80px;
                font-weight: 700;
                color: white;
                line-height: 28px;
                text-align: center;
                margin-right: 15px;
                cursor: default;
            }
        }
    }
    .left {
        position: absolute;
        left: 0;
        top: 0;
        height: calc(100% - 50px);
        width: 400px;
        display: flex;
        justify-content: center;
        align-items: center;
        .tit {
            width: 100%;
            height: 40px;
            position: absolute;
            top: 12px;
            left: 0;
            color: white;
            line-height: 40px;
            text-align: center;
            font-size: 20px;
            font-weight: 700;
        }
        .con {
            width: 230px;
            height: 550px;
            overflow-y: auto;
            padding: 5px 15px;
            &::-webkit-scrollbar {
                display: none;
            }
            .item {
                width: 200px;
                height: 180px;
                margin-bottom: 70px;
                position: relative;
                &::before {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 20px;
                    height: 20px;
                    left: -3.5px;
                    top: -3.5px;
                    border-top: 3.5px solid rgb(0, 247, 255);
                    border-left: 3.5px solid rgb(0, 247, 255);
                }
                &::after {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 20px;
                    height: 20px;
                    right: -3.5px;
                    top: -3.5px;
                    border-top: 3.5px solid rgb(0, 247, 255);
                    border-right: 3.5px solid rgb(0, 247, 255);
                }
                .time {
                    width: 100%;
                    height: 15px;
                    color: white;
                    line-height: 15px;
                    text-align: center;
                    overflow: hidden;
                    font-size: 14px;
                }
                .image {
                    width: 100%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    img {
                        width: 158px;
                        height: 158px;
                    }
                }
                .bot {
                    &::before {
                        display: block;
                        position: absolute;
                        content: '';
                        width: 20px;
                        height: 20px;
                        left: -3.5px;
                        bottom: -3.5px;
                        border-bottom: 3.5px solid rgb(0, 247, 255);
                        border-left: 3.5px solid rgb(0, 247, 255);
                    }
                    &::after {
                        display: block;
                        position: absolute;
                        content: '';
                        width: 20px;
                        height: 20px;
                        right: -3.5px;
                        bottom: -3.5px;
                        border-bottom: 3.5px solid rgb(0, 247, 255);
                        border-right: 3.5px solid rgb(0, 247, 255);
                    }
                }
            }
            .current {
                box-shadow: 3px 3px 6px 2px #7ccccf;
            }
        }
    }

    .center {
        margin: 0 auto;
        width: 708px;
        height: calc(100% - 50px);
        -webkit-user-drag: none;     
        img {
            width: 708px;
            height: 708px;
            -webkit-user-drag: none;
        }
       
    }

    .right {
        position: absolute;
        top: 0;
        right: 0;
        width: 400px;
        height: calc(100% - 50px);
        display: flex;
        justify-content: center;
        align-items: center;
        .con {
            width: 290px;
            height: 300px;
            padding: 25px 15px;         
            border-radius: 8px;
            color: #abd4fd;
            background-color: #0F3A65;
            .item {
                width: 100%;
                height: 35px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 17px;
                margin-bottom: 7px;
                .one {
                    width: 10px;
                    flex: 1;
                    height: 35px;
                    line-height: 35px;
                    padding-left: 5px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .two {
                    width: 10px;
                    flex: 1;
                    height: 35px;
                    line-height: 35px;
                    padding-left: 5px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    .chaochang {
                        width: 38px;
                        height: 21px;
                        background: rgb(0, 115, 225);
                    }
                    .youguan {
                        width: 38px;
                        height: 21px;
                        background: rgb(83, 255, 98);
                    }
                    .feiji {
                        width: 38px;
                        height: 21px;
                        background: rgb(255, 255, 255);
                    }
                    .lijiaoqiao {
                        width: 38px;
                        height: 21px;
                        background: rgb(255, 189, 57);
                    }
                }
                .three {
                    flex: 1;
                    width: 10px;
                    height: 35px;
                    line-height: 35px;
                    padding-left: 5px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    .no {
                        width: 100%;
                        height: 100%;
                        line-height: 35px;
                        text-align: center;
                    }
                    .isshow {
                        width: 24px;
                        height: 24px;
                        img {
                            width: 100%;
                            height: 100%;
                        }
                    }
                }
                .head {
                    font-size: 17.5px;
                    color: #ffffff;
                }
            }
        }
    }
</style>