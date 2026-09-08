<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="line-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="slider">
      <div class="w-100 px-2">
    <v-slider
      label=""
    ></v-slider>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="5" offset="0">
<div obj="line-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="5" offset="1">
<div obj="bar-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="textarea">
      <div class="w-100 px-2">
    <v-textarea
      bg-color="white"
      class="w-100"
      density="compact"
      label="0"
      style="height: 103px;"
      variant="outlined"
    ></v-textarea>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="9" offset="1">
<div obj="pie-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="slider">
      <div class="w-100 px-2">
    <v-slider
      label=""
    ></v-slider>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="1" offset="0">
<div obj="radio-button">
      <div class="w-100 px-2">
    <v-radio
      class="w-100"
      density="compact"
      label="Radio Button"
      hide-details
    ></v-radio>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="1">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="3" offset="1">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="switch">
      <div class="w-100 px-2">
    <v-switch
      color="primary"
      class="w-100 pl-1"
      density="compact"
      label=""
      hide-details
    ></v-switch>
  </div>

</div>
			</v-col>
		</v-row>
    </v-container>
</template>
<script setup lang="ts">
    import {onMounted, onBeforeUnmount, ref} from 'vue'
    import Chart from '@/components/Chart.vue'
    
    onMounted(() => {
    })
    onBeforeUnmount(() => {
    })
</script>
