require 'test_helper'

class AesControllerTest < ActionDispatch::IntegrationTest
  test "should get home" do
    get aes_home_url
    assert_response :success
  end

end
