<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="3" offset="0">
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
			<v-col cols="4" offset="0">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="date-picker">
      <div class="w-100 px-2">
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="auto"
    >
      <template #activator="{ props }">
        <v-text-field
          v-bind="props"
          v-model="selectedDate"
          label=""
          append-inner-icon="mdi-calendar"
          readonly
          density="compact"
          hide-details
          variant="outlined"
        ></v-text-field>
      </template>

      <v-date-picker
        v-model="selectedDate"
        @update:model-value="menu = false"
        color="primary"
      ></v-date-picker>
    </v-menu>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="time-picker">
      <div class="w-100 px-2">
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="auto"
    >
      <template #activator="{ props }">
        <v-text-field
          v-bind="props"
          v-model="selectedDate"
          label=""
          append-inner-icon="mdi-calendar"
          readonly
          density="compact"
          hide-details
          variant="outlined"
        ></v-text-field>
      </template>

      <v-date-picker
        v-model="selectedDate"
        @update:model-value="menu = false"
        color="primary"
      ></v-date-picker>
    </v-menu>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
<div obj="list">
    <div>
    <v-table
      density="compact"
      class="table"
      style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      
      
      <tbody>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
</tbody>

    </v-table>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 212px;
                 width: 167px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 206px;
                 width: 158px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 205px;
                 width: 157px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 196px;
                 width: 164px;
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
			<v-col cols="1" offset="0">
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
			<v-col cols="3" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 33px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 239px;
                 width: 164px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 224px;
                 width: 159px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 210px;
                 width: 159px;
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
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 219px;
                 width: 178px;
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
			<v-col cols="4" offset="0">
<div obj="input-number">
      <div class="w-100 px-2">
    <v-text-field
      bg-color="white"
      class="w-100"
      density="compact"
      label="0"
      type="number"
      variant="outlined"
    ></v-text-field>
  </div>

</div>
<div obj="bar-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="6" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 231px;
                 width: 167px;
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
<div obj="segmented-button">
        <div class='ui-segmented-button'>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 243px;
                 width: 175px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 246px;
                 width: 159px;
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
			<v-col cols="2" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 218px;
                 width: 166px;
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
    </v-container>
</template>
<script setup lang="ts">
    import {onMounted, onBeforeUnmount, ref} from 'vue'
    import Chart from '@/components/Chart.vue'
    const menu = ref(false)
const selectedDate = ref('')

    onMounted(() => {
    })
    onBeforeUnmount(() => {
    })
</script>
