
<template>
	<div id="chart"></div>
</template>
<script>
export default {
    name: 'Home',
    mounted() {
        this.$chart.first_bar('chart'); //方法调用
    }
}
</script>

<style scoped>
    #chart {
        width: 300px;
        height: 300px;
    }
</style>
