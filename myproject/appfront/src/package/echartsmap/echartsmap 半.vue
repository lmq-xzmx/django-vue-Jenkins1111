<template>

  <div>
    <h2>这次要画地图了</h2>
<!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
    <div id="echartMap" style="width:60%;height:90%"></div> 
    </div>
</template>
 
<script>
  import * as echarts from 'echarts';


  export default {
    name: "echarts",
        data(){                    
             return{            
                batchId:'',            
                areaData:[],                  
                dalian: require('@/assets/json/dalian.json')        //地图json数据
            }    
        }, 

        
    mounted() {


      // 使用刚指定的配置项和数据显示图表。
      //myChart.setOption(option);
      //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
      //window.addEventListener('resize',function() {myChart.resize()});
    },
    beforeDestroy() {

        },
    methods: {
        init(dalian){
                    this.$nextTick(()=>{
                      var myChart = this.$echarts.init(document.getElementById('echartMap'));
                      echarts.registerMap('dalian', dalian,{});
                      myChart.setOption({
                        series: [{
                            name:'大连市',
                            label: {
                                normal: {
                                  show: true,
                                },
                                emphasis: {
                                    show: true
                                }
                            },
                            itemStyle: {
                                color: '#ddb926'
                            },
                            type: 'map',
                            zoom: 1,//缩放比例
                            roam: true,
                            mapType: 'dalian',
                            emphasis: {
                                label: {
                                    show: true
                                }
                            },
                            // 文本位置修正
                            textFixed: {
                                Alaska: [20, -20]
                            },
                            data: [{
                                     name: '瓦房店市',
                                     value: 4822023
                                 },
                                 {
                                     name: '旅顺口区',
                                     value: 9317568
                                 }
                             ]
                        }],
                        //右下角数值条
                        visualMap: {
                            left: 'right',
                            min: 1,
                            max: 100,
                            inRange: {
                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                            },
                            //text: ['High', 'Low'], // 文本，默认为数值文本
                            calculable: true
                        },
                        tooltip: {
                            trigger: 'item',       
                            showDelay: 0,      
                            transitionDuration: 0.2,
                            formatter: function(params) {
                                var value = (params.value + '').split('.');
                                value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');
                                return params.seriesName + '<br/>' + params.name + ': ' + value;
                            }
                        },
                    });
                    })
                }
    },
    watch: {},
    created() {
    }
  }
</script>
