import './App.css'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-0">
      <div className="mx-auto max-w-md rounded bg-white p-6 shadow">

        {/* Row 1 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-6 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 2 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
        </div>

        {/* Row 3 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-8 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping alert */}<div obj="alert">
                  <div className="w-full rounded border border-amber-300 bg-amber-50 px-4 py-3 text-amber-900">
                <div className="flex items-start gap-2">
                  <span className="text-lg leading-none">!</span>
                  <div>Alert</div>
                </div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 4 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-8 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping alert */}<div obj="alert">
                  <div className="w-full rounded border border-amber-300 bg-amber-50 px-4 py-3 text-amber-900">
                <div className="flex items-start gap-2">
                  <span className="text-lg leading-none">!</span>
                  <div>Alert</div>
                </div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 5 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-8 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping alert */}<div obj="alert">
                  <div className="w-full rounded border border-amber-300 bg-amber-50 px-4 py-3 text-amber-900">
                <div className="flex items-start gap-2">
                  <span className="text-lg leading-none">!</span>
                  <div>Alert</div>
                </div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 6 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-1 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping checkbox */}<div obj="checkbox">
                  <input type="checkbox" className="h-5 w-5" />

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-4 col-start-5">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
