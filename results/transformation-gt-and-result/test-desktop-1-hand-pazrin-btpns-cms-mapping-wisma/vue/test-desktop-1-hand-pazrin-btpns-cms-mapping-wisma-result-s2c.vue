<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 68px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="3" offset="6">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 53px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="3" offset="0">
<div obj="combobox">
      <div class="w-100 px-2">
    <v-combobox
      density="compact"
      label=""
      :items="[]"
      variant="outlined"
    ></v-combobox>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="1">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
			<v-col cols="2" offset="1">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

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
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
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
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr>
</tbody>

    </v-table>
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
