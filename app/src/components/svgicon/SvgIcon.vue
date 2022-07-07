<template>
  <svg :class="svgClass">
    <use :xlink:href="iconName"/>
  </svg>
</template>

<script>
  export default {
    name: 'SvgIcon',
    props: {
      iconClass: {
        type: String,
        required: true
      },
      className: {
        type: String,
        default: ''
      }
    },
    computed: {
      iconName() {
        return `#icon-${this.iconClass}`
      },
      svgClass() {
        if (this.className) {
          return this.className + ' svg-icon' 
        } else {
          return 'svg-icon'
        }
      }
    }
  }
</script>
 
<style scoped>
  .svg-icon {
    width: 2em;
    height: 2em;
    vertical-align: middle;
    /* 默认读取父级颜色 */
    fill: currentColor;
    overflow: hidden;
  }
</style>