<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="6" offset="2">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 85px;
                 width: 190px;
                 border-radius: 10px;
                 box-shadow: 0 2px 6px rgba(0,0,0,0.15);
                 background-color: #fff;
                 display: flex;
                 flex-direction: column;
                 align-items: center;
                 overflow: hidden">
             <div style="width: 100%;height: 100%;flex: 1;display: flex;align-items: center;justify-content: center" class="w-100">
                     <div
        style="
          border: 1px solid #eee;
          width: 100%;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px
        ">
        <span style="font-size: 20px;">
          <v-icon icon="mdi-image-area"></v-icon>
        </span>
    <div>Image</div>
  </div>

             </div>
             <div style="line-height: 100%; padding: 8px 12px;text-align: left;font-size: 16px;font-weight: 500;color: #333;width: 100%;box-sizing: border-box">Title</div>
             
       </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="2">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="8" offset="2">
<div obj="common-image-button">
        <div class='ui-common-image-button'>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="8" offset="2">
<div obj="common-image-button">
        <div class='ui-common-image-button'>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="8" offset="2">
<div obj="common-image-button">
        <div class='ui-common-image-button'>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="1" offset="2">
<div obj="checkbox">
      <div class="w-100 px-2">
    <v-checkbox
      class="w-100"
      density="compact"
      label="Checkbox"
      hide-details
    ></v-checkbox>
  </div>

</div>
			</v-col>
			<v-col cols="4" offset="1">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
		</v-row>
    </v-container>
</template>
<script setup lang="ts">
    import {onMounted, onBeforeUnmount, ref} from 'vue'
    
    
    onMounted(() => {
    })
    onBeforeUnmount(() => {
    })
</script>
