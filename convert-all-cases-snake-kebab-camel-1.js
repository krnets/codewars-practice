function changeCase(identifier, targetCase) {
    let isKebabCase = identifier.includes('-')
    let isCamelCase = identifier.split('')
        .filter(v => v.toUpperCase() === v && v !== '_' && v !== '-').length > 0
    let isSnakeCase = identifier.includes('_')
    let t = targetCase.match(/(snake|camel|kebab)/)
    let newString = ''

    if ((isKebabCase + isCamelCase + isSnakeCase) > 1 || t == null) {
        return undefined
    }
    if (identifier.length == 0) {
        return ""
    }

    if (targetCase == 'snake') {
        for (let i = 0; i < identifier.length + 1; i++) {
            newString += identifier.slice(i - 1, i)
            // already snake? continue
            if (isSnakeCase) {
                continue
            }
            // from kebab
            if (isKebabCase && identifier[i] == '-') {
                newString += '_'
                i++
            }
            // from camelCase
            if (identifier[i] !== undefined && identifier[i] === identifier[i].toUpperCase() &&
                identifier[i + 1] !== undefined && identifier[i + 1] === identifier[i + 1].toUpperCase() &&
                identifier[i + 2] !== undefined && identifier[i + 2] === identifier[i + 2].toUpperCase()) {
                newString += '_'
                newString += identifier[i].toLowerCase()
                newString += '_'
                newString += identifier[i + 1].toLowerCase()
                newString += '_'
                newString += identifier[i + 2].toLowerCase()
                i += 3
            }
            if (identifier[i] !== undefined && identifier[i] === identifier[i].toUpperCase() &&
                identifier[i + 1] !== undefined && identifier[i + 1] === identifier[i + 1].toUpperCase()) {
                newString += '_'
                newString += identifier[i].toLowerCase()
                newString += '_'
                newString += identifier[i + 1].toLowerCase()
                i += 2
            }
            if (identifier[i] !== undefined && identifier[i] === identifier[i].toUpperCase()) {
                newString += '_'
                newString += identifier[i].toLowerCase()
                i++
            }
        }
        return newString
    }


    if (targetCase == 'camel') {
        for (let i = 0; i < identifier.length + 1; i++) {
            newString += identifier.slice(i - 1, i)
            // from snake_case
            if (isSnakeCase && identifier[i] == '_' && identifier[i + 1] != undefined &&
                identifier[i + 2] == '_' && identifier[i + 3] != undefined) {
                newString += identifier[i + 1].toUpperCase()
                newString += identifier[i + 3].toUpperCase()
                i = i + 4
            }

            if (isSnakeCase && identifier[i] == '_' && identifier[i + 1] != undefined) {
                newString += identifier[i + 1].toUpperCase()
                i = i + 2
            }

            // from kebab case : abc-d-e-f-gha -> abcDEFgha 
            if (isKebabCase && identifier[i] == '-' && identifier[i + 1] != undefined &&
                identifier[i + 2] == '-' && identifier[i + 3] != undefined &&
                identifier[i + 4] == '-' && identifier[i + 5] != undefined) {
                newString += identifier[i + 1].toUpperCase()
                newString += identifier[i + 3].toUpperCase()
                newString += identifier[i + 5].toUpperCase()
                i = i + 6
            }

            if (isKebabCase && identifier[i] == '-' && identifier[i + 1] != undefined &&
                identifier[i + 2] == '-' && identifier[i + 3] != undefined) {
                newString += identifier[i + 1].toUpperCase()
                newString += identifier[i + 3].toUpperCase()
                i = i + 4
            }

            if (isKebabCase && identifier[i] == '-' && identifier[i + 1] != undefined) {
                newString += identifier[i + 1].toUpperCase()
                i = i + 2
            }
        }
        return newString
    }

    if (targetCase == 'kebab') {
        for (let i = 0; i < identifier.length + 1; i++) {
            newString += identifier.slice(i - 1, i)
            // from snake_case
            if (isSnakeCase && identifier[i] == '_') {
                newString += '-'
                i++
            }

            if (identifier[i] != undefined && identifier[i] == identifier[i].toUpperCase() &&
                identifier[i + 1] != undefined && identifier[i + 1] == identifier[i + 1].toUpperCase() &&
                identifier[i + 2] != undefined && identifier[i + 2] == identifier[i + 2].toUpperCase() &&
                identifier[i + 3] != undefined && identifier[i + 3] == identifier[i + 3].toUpperCase() &&
                identifier[i + 4] != undefined && identifier[i + 4] == identifier[i + 4].toUpperCase() &&
                identifier[i + 5] != undefined && identifier[i + 5] == identifier[i + 5].toLowerCase()) {
                newString += '-'
                newString += identifier[i].toLowerCase()
                newString += '-'
                newString += identifier[i + 1].toLowerCase()
                newString += '-'
                newString += identifier[i + 2].toLowerCase()
                newString += '-'
                newString += identifier[i + 3].toLowerCase()
                newString += '-'
                newString += identifier[i + 4].toLowerCase()
                newString += identifier[i + 5]
                i += 6
            }
            if (identifier[i] != undefined && identifier[i] == identifier[i].toUpperCase() &&
                identifier[i + 1] != undefined && identifier[i + 1] == identifier[i + 1].toUpperCase() &&
                identifier[i + 2] != undefined && identifier[i + 2] == identifier[i + 2].toUpperCase() &&
                identifier[i + 3] != undefined && identifier[i + 3] == identifier[i + 3].toUpperCase() &&
                identifier[i + 4] != undefined && identifier[i + 4] == identifier[i + 4].toLowerCase()) {
                newString += '-'
                newString += identifier[i].toLowerCase()
                newString += '-'
                newString += identifier[i + 1].toLowerCase()
                newString += '-'
                newString += identifier[i + 2].toLowerCase()
                newString += '-'
                newString += identifier[i + 3].toLowerCase()
                newString += identifier[i + 4]
                i += 5
            }
            if (identifier[i] != undefined && identifier[i] == identifier[i].toUpperCase() &&
                identifier[i + 1] != undefined && identifier[i + 1] == identifier[i + 1].toUpperCase() &&
                identifier[i + 2] != undefined && identifier[i + 2] == identifier[i + 2].toUpperCase() &&
                identifier[i + 3] != undefined && identifier[i + 3] == identifier[i + 3].toLowerCase()) {
                newString += '-'
                newString += identifier[i].toLowerCase()
                newString += '-'
                newString += identifier[i + 1].toLowerCase()
                newString += '-'
                newString += identifier[i + 2].toLowerCase()
                newString += identifier[i + 3]
                i += 4
            }

            if (identifier[i] != undefined && identifier[i] == identifier[i].toUpperCase() &&
                identifier[i + 1] != undefined && identifier[i + 1] == identifier[i + 1].toUpperCase() &&
                identifier[i + 2] != undefined && identifier[i + 2] == identifier[i + 2].toLowerCase()) {
                newString += '-'
                newString += identifier[i].toLowerCase()
                newString += '-'
                newString += identifier[i + 1].toLowerCase()
                newString += identifier[i + 2]
                i += 3
            }

            if (identifier[i] != undefined && identifier[i] == identifier[i].toUpperCase() &&
                identifier[i + 1] != undefined && identifier[i + 1] == identifier[i + 1].toUpperCase()) {
                newString += '-'
                newString += identifier[i].toLowerCase()
                newString += '-'
                newString += identifier[i + 1].toLowerCase()
                i += 2
            }

            if (identifier[i] != undefined && identifier[i] == identifier[i].toUpperCase() && identifier[i] != '-') {
                newString += '-'
                newString += identifier[i].toLowerCase()
                i++
            }
        }
        return newString
    }
    return 'no cases matched'
}

// q = changeCase("little-shop-of-horrors", "kebab") // 'little-shop-of-horrors'
// q
// q = changeCase("doHTMLrequest", "kebab") // "do-h-t-m-l-request"
// q
// q = changeCase("doHTMLRequest", "kebab") // "do-h-t-m-l-request"
// q
// q = changeCase("fromCamelCase", "kebab") // "from-camel-case"
// q
// q = changeCase("fromCamelCase", "snake") // "from_camel_case")
// q
// q = changeCase("from-kebab-case", "snake") // "from_kebab_case"
// q
// q = changeCase("little_shop_of_horrors", "snake") // 'little_shop_of_horrors'
// q
// q = changeCase("from_snake_case", "camel") // "fromSnakeCase"
// q
// q = changeCase("from-kebab-case", "camel") // "fromKebabCase"
// q
// q = changeCase("from-k-e-b-ab-case", "camel") // "fromKebabCase"
// q
// q = changeCase("guluznumosyet-i-ojfkcmolqikg-wcszrjummr", "camel") // "guluznumosyetIOjfkcmolqikgWcszrjummr"
// q
// q = changeCase("from_snake_case", "kebab") // "from-snake-case"
// q
// q = changeCase("invalid-inPut_bad", "kebab") // undefined
// q
// q = changeCase("valid-input", "huh???") // undefined
// q
// q = changeCase("", "camel") // ""
// q




// Failed while converting from camel to snake - 
// Expected: 'wm_w_k_xem_xr_du_pca_waeahqmxro', 
// tead got: 'wm_wK_xem_xr_du_pca_waeahqmxro'
// q = changeCase("wmWKXemXrDuPcaWaeahqmxro", "snake")
// q
// wm_wK_xem_xr_du_pca_waeahqmxro

// Failed while converting from camel to snake - 
// q = changeCase('qHUdfwyzvslkp','snake') // Expected: 'q_h_udfwyzvslkp', 
// instead got: 'q_h_ufwyzvslkp
// q

// Failed while converting from snake to camel - 
// Expected: 'fSLxexyBbxmzvtkqappCnmcmjnbpZnmqSmnwewtom', 
// tead got: 'fS_lxexyBbxmzvtkqappCnmcmjnbpZnmqSmnwewtom'

// Failed while converting from snake to camel - 
// Expected: 'akynfdtqciDlcoftdkhwyAtblpNvozakejxWdchmipablafYbkrxjdYikdMLonIqzmvkm', 
// tead got: 'akynfdtqciDlcoftdkhwyAtblpNvozakejxWdchmipablafYbkrxjdYikdM_lonIqzmvkm'

// Unhandled rejection TestError: Failed while converting from snake to camel - 
// q = changeCase("apdohzyxtg_aoax_ukrkrd_unxi_n_zkau_vqekudd_jgadvrujb", "camel")
// Expected: 'jwuapdohzyxtgAoaxUkrkrdUnxiNZkauVqekuddJgadvrujb', 
// instead got: 'jwuapdohzyxtgAoaxUkrkrdUnxiN_zkauVqekuddJgadvrujb'
// q

// Failed while converting from kebab to camel - 
// Expected: 'jbkzsmimMrzarcdtmEnnqzcuwAgreeuwcpxSMYcuqlqahmauVaklwSH', 
// instead got: 'jbkzsmimMrzarcdtmEnnqzcuwAgreeuwcpxSM-ycuqlqahmauVaklwSH'
// q = changeCase('jbkzsmim-mrzarcdtm-ennqzcuw-agreeuwcpx-s-m-ycuqlqahmau-vaklw-s-h', 'camel')
// q
// q = changeCase('ime-s-m-y-cu-vaklw-s-h', 'camel')
// q

// Failed while converting from snake to camel - 
// Expected: 'esqksipnWdnrvztnuzsvZvoldJXLttamptifSgrGemzucyzMoFidjbrvrb', 
// tead got: 'esqksipnWdnrvztnuzsvZvoldJX_lttamptifSgrGemzucyzMoFidjbrvrb'
// q = changeCase('esqksipn_wdnrvztnuzsv_zvold_j_x_ltamptif_sgr_gemzucyz_mo_fidjbrvrb', 'camel')
// q
// q = changeCase('en_j_x_lt', 'camel')
// q
// Failed while converting from camel to snake - 
// Expected: 'mzn_zb_i_o_u_v_fd_yuqocwh', 
// tead got: 'mzn_zb_i_o_uV_fd_yuqocwh'


// 3 cases: snake_case, kebab, camelCase
// snake_case: from camelCase, kebab
// kebab: from camelcase, snake_case
// camelCase: from kebab, snake_case