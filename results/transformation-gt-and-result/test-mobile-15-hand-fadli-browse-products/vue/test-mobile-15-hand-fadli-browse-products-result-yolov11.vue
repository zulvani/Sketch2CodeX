<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="12" offset="0">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 160px;
                 width: 381px;
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
			<v-col cols="3" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
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
			<v-col cols="3" offset="0">
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
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
</tbody>

    </v-table>
  </div>

</div>
<div obj="undefined">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 114px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="3" offset="3">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 115px;
                 width: 93px;
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
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="2" offset="5">
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
		<v-row style="margin-top: 0px">
			<v-col cols="6" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 190px;
                 width: 189px;
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
			<v-col cols="6" offset="0">
<div obj="image-card">
           <div class="ui-image-card w-100 d-flex align-center justify-center"
                 style="
                 height: 185px;
                 width: 191px;
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
			<v-col cols="3" offset="0">
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
			</v-col>
			<v-col cols="3" offset="1">
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
			</v-col>
			<v-col cols="4" offset="0">
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
			<v-col cols="1" offset="8">
<div obj="table">
    <div>
    <v-table
      density="compact"
      class="table"
      style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      
      <thead><tr>
<th>Header 1</th>
<th>Header 2</th>
<th>Header 3</th>
</tr></thead>

      <tbody>
</tbody>

    </v-table>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="undefined">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 51px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
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
