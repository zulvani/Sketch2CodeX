<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="5" offset="1">
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
			<v-col cols="10" offset="1">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="10" offset="1">
<div obj="input-password">
      <div class="w-100 px-2">
    <v-text-field
      bg-color="white"
      class="w-100"
      density="compact"
      label="Password"
      type="password"
      variant="outlined"
    ></v-text-field>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="6" offset="2">
<div obj="alert">
      <v-alert>
  <div class="ui-alert">
    Alert
  </div>
  </v-alert>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="1" offset="1">
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
			<v-col cols="8" offset="0">
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
			<v-col cols="10" offset="1">
<div obj="textarea">
      <div class="w-100 px-2">
    <v-textarea
      bg-color="white"
      class="w-100"
      density="compact"
      label="0"
      style="height: 218px;"
      variant="outlined"
    ></v-textarea>
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
