<template>

  <div>
    <h2>信息统计柱形图</h2>
<!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
    <div id="main" style="width: 600px;height:400px;"></div>

    <p>template已经加载，id=main get-id时要记得 </p>  
  </div>
</template>
 
<script>
  import * as echarts from 'echarts';
  
  export default {
    data() {
      return {}
    },
    mounted() {
      //let this_ = this;
      let myChart = echarts.init(document.getElementById('main'));
  
      let option = {
        title: {
                text: 'ECharts 入门示例'
                },
        tooltip: {},
        legend: {
                data:['销量']
                    },
        xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
                    },
        yAxis: {},
        series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
                }]
        };

      // 使用刚指定的配置项和数据显示图表。
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
