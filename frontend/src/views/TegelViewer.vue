<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>{{appName}} - Viewer</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <p class="subheading">{{currentWijsheid.content}}</p>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="refresh">Refresh</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import { api } from '@/api';
import { Vue, Component, Prop, Watch } from 'vue-property-decorator';
import { AppWijsheid } from '@/store/main/state';
import { readWijsheid } from '@/store/main/getters';
import { dispatchGetWijsheid } from '@/store/main/actions';

import { appName } from '@/env';


@Component
export default class Login extends Vue {
  public valid = true;
  public username: string = '';
  public appName = appName;
  public currentWijsheid: AppWijsheid = { content: 'TegelViewer.vue wijsheid'};
  public watchtest: string = 'foo';

  public async refresh() {
    // TODO: use proper vuex store things
    // dispatchGetWijsheid(this.$store);
    // await this.setWijsheid({ content: 'refresh wijsheid' });
    var wijsheid = api.getWijsheid();
    await this.setWijsheid({ content: (await wijsheid).data.msg })

  }

  public get firstWijsheid() {
      return readWijsheid(this.$store);
  }

  public get watchtestfn() {
    return this.watchtest;
  }

  public async setWijsheid(wijsheid: AppWijsheid | false) {
      if (wijsheid) {
          this.currentWijsheid = wijsheid;
      } else {
          this.currentWijsheid = { content: '' };
      }
  }

  @Watch('firstWijsheid')
  public async onWijsheidChange(Wijsheid: AppWijsheid) {
      // await this.setWijsheid(Wijsheid);
      this.currentWijsheid = { content: "watchtestfn fired" };
  }

}
</script>

<style>
</style>
