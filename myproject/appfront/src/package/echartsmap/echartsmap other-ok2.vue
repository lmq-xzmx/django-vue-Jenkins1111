<template>

  <div>
    <h2>信息统计柱形图</h2>
    <div id="chart_example" class="chart_example" ></div>   
	
	<p>template已经加载</p>
  </div>
</template>
 
<script >
  import * as echarts from 'echarts';
  
  export default {
    data() {
      return {}
    },
    mounted() {
      //let this_ = this;
      let myChart = echarts.init(document.getElementById('chart_example'));
      let option = {
        color: ['#72ccff'],
        tooltip : {
          trigger: 'axis',
          axisPointer : {
            type : 'shadow'
          }
        },
        xAxis : [
          {
            type : 'category',
            data : ['周日','周一','周二','周三','周四','周五','周六',],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis : [
          {
            type : 'value'
          }
        ],
        series : [
          {
            name:'每月花费',
            type:'bar',
            barWidth: '60%',
            data:[995,666,444,858,654,236,645]
          }
        ]
      };
      myChart.setOption(option);
 
      //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
      window.addEventListener('resize',function() {myChart.resize()});
    },
    methods: {},
    watch: {},
    created() {
 
    }
  }
</script>

<style scoped>
  h2{
    text-align: center;
    padding: 30px;
    font-size: 18px;
  }
  #chart_example{
    width: 50%;
    height: 500px;
    border: 1px solid #72ccff;
    margin: 0 auto;
  }

</style>