(function() {
  'use strict';

  angular
    .module('rthmdance')
    .run(runBlock);

  /** @ngInject */
  function runBlock($log) {

    $log.debug('runBlock end');
  }

})();
