//
//  Inson_va_kompyuterning_o_zaro_ta_siri_2UITestsLaunchTests.swift
//  Inson_va_kompyuterning_o'zaro_ta'siri_2UITests
//
//  Created by Diyorbek Xikmatullayev on 28/10/24.
//

import XCTest

final class Inson_va_kompyuterning_o_zaro_ta_siri_2UITestsLaunchTests: XCTestCase {

    override class var runsForEachTargetApplicationUIConfiguration: Bool {
        true
    }

    override func setUpWithError() throws {
        continueAfterFailure = false
    }

    @MainActor
    func testLaunch() throws {
        let app = XCUIApplication()
        app.launch()

        // Insert steps here to perform after app launch but before taking a screenshot,
        // such as logging into a test account or navigating somewhere in the app

        let attachment = XCTAttachment(screenshot: app.screenshot())
        attachment.name = "Launch Screen"
        attachment.lifetime = .keepAlways
        add(attachment)
    }
}
